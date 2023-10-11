from django import forms
from django.forms import ImageField
from django.template import Template

from generator.models import Picture

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('description', 'picture',)
