import os

from django.shortcuts import render, redirect

from memegenerator.settings import BASE_DIR
from .models import Picture, Meme
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

from .forms import PictureForm
# Create your views here.

def handle_uploaded_file(file):
    with open(file, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

# unused, need to update
# def create_meme(file,text):
#
#     image = Image.open(file.path)
#     path = os.path.join(BASE_DIR,'generator/memes/')
#     font = ImageFont.truetype("arial.ttf", 50)
#     drawer = ImageDraw.Draw(image)
#     drawer.text((50, 100), text, font=font, fill='white')
#     full_path = os.path.join(path, f"processed_{file.name.split('/')[-1]}")
#     # print(full_path)
#     image.save(full_path)
#     # image.show()
#     return full_path



def apply_text(file,text):

    path = os.path.join(BASE_DIR, 'generator/memes/')

    image = Image.open(file.path)
    draw = ImageDraw.Draw(image)
    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 0.95

    font = ImageFont.truetype("impact.ttf", fontsize)

    while font.getsize(text)[0] < img_fraction * image.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("arial.ttf", fontsize)

    fontsize -= 1
    font = ImageFont.truetype("impact.ttf", fontsize)

    draw.multiline_text((image.size[0] * 0.05,image.size[1]*0.8),
                        # stroke_width=3,stroke_fill ='black',
                        text=text,font=font,align='center')

    full_path = os.path.join(path, f"processed_{file.name.split('/')[-1]}")
    image.save(full_path)
    # image.show()
    return full_path




def create_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            obj = form.save()
            file = obj.picture
            # meme_link = create_meme(file,obj.description)
            meme_link = apply_text(file, obj.description)
            Meme.objects.update_or_create(picture_ref=Picture.objects.get(pk=obj.pk), meme_picture=meme_link)

            return redirect('pictures_list')  # Redirect to the object list view
    else:
        form = PictureForm()
    return render(request, 'create_picture.html', {'form': form})

def pictures_list(request):
    p_list = Picture.objects.all()  # Replace with your model's name
    return render(request, 'pictures_list.html', {'p_list': p_list})

def get_picture(request, pk):
    picture_detail = Picture.objects.get(pk=pk)  # Replace with your model's name
    return render(request, 'picture_detail.html', {'picture_detail': picture_detail})


