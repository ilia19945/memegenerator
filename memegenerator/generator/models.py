from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Picture(models.Model):
    date = models.DateTimeField("date",auto_now_add=True)
    date_updated = models.DateTimeField("date_updated",auto_now=True)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    picture = models.ImageField(upload_to='generator/pictures')

    def __str__(self):
        return f'{self.pk}, {self.picture.__sizeof__()} Kb'

class Meme(models.Model):
    date_processed = models.DateTimeField("date",auto_now_add=True)
    meme_picture = models.ImageField(upload_to='generator/memes')
    picture_ref = models.ForeignKey(Picture, null=True, blank=True,on_delete=models.CASCADE)