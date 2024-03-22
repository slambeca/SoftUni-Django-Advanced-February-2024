from django.db import models

from Petstagram.photos.models import PetPhoto


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.RESTRICT,
    )

    # user = models.ForeignKey(User)


class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        PetPhoto, on_delete=models.DO_NOTHING
    )

    # user = models.ForeignKey(User)

# photo_like = PhotoLike.objects.filter(pet_photo_id=pet_photo.pk, user=request.user)