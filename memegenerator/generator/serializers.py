# Serializers define the API representation.
from rest_framework import serializers
from generator.models import Picture


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Picture
        fields = ('pk','date', 'date_updated', 'description','user', 'picture')
        lookup_field = ('pk','user')




