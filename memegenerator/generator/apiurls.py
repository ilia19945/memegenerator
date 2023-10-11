
from django.urls import path, include
from .apiviews import PicturesViewGet,PicturesViewUpdate,PicturesViewDelete

# router = DefaultRouter()
#
# router.register('detail/<int:pk>',PicturesViewGet, basename='pictures-detail')
# router.register('list',PicturesViewGet, basename='pictures-list')
# router.register('update/<int:pk>',PicturesViewUpdate, basename='pictures-update')
# router.register('delete/<int:pk>',PicturesViewDelete, basename='pictures-delete')

urlpatterns = [
    path('picture/detail/<int:pk>',PicturesViewGet.as_view({'get': 'retrieve'})),
    path('pictures/',PicturesViewGet.as_view({'get': 'list','post': 'create'})),
    path('picture/update/<int:pk>',PicturesViewUpdate.as_view({'get': 'retrieve','put': 'update'})),
    path('picture/delete/<int:pk>',PicturesViewDelete.as_view({'get': 'retrieve', 'delete': 'destroy'})),
] # + router.urls

