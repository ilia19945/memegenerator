from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import create_picture, get_picture,pictures_list
urlpatterns = [
    path('detail/<int:pk>',get_picture, name='get_picture'),
    path('',pictures_list, name ='pictures_list'),
    path('delete/<int:pk>',get_picture, name='get_picture'),
    path('upload/',create_picture, name='create_picture'),
]




