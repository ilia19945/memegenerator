
from rest_framework import viewsets, permissions
from memegenerator.permissions import IsOwnerOrView

from .models import Picture
from .serializers import PictureSerializer


class PicturesViewGet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PicturesViewUpdate(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = (IsOwnerOrView,)


class PicturesViewDelete(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = (IsOwnerOrView,)
