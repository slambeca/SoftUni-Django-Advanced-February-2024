from django.urls import path

from Petstagram.photos.views import PetPhotoCreateView, PetPhotoDetailView, PetPhotoEditView


urlpatterns = (
    path("create/", PetPhotoCreateView.as_view(), name="create photo"),
    path("<int:pk>/", PetPhotoDetailView.as_view(), name="details photo"),
    path("<int:pk>/edit/", PetPhotoEditView.as_view(), name="edit photo"),
)