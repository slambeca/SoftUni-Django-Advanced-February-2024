from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.pets.models import Pet

# This code is more flexible
# class MaxFileSizeValidator(BaseValidator):
#     def clean(self, x):
#         return x.size
#
#     def compare(self, file_size, max_size):
#         return max_size < file_size

UserModel = get_user_model()


SIZE_5MB = 5 * 1024 * 1024


def image_size_less_than_5mb_validator(some_image):
    if some_image.size > SIZE_5MB:
        raise ValidationError("The size of the image cannot exceed 5 mb!")


class PetPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to="pet_photos/",
        blank=False,
        null=False,
        validators=(
            image_size_less_than_5mb_validator,
            # MaxFileSizeValidator(limit_value=SIZE_5MB),
        )
    )

    description = models.TextField(
        blank=True,
        null=True,
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    pets = models.ManyToManyField(Pet)

    # created_at = models.DateTimeField(
    #     auto_now_add=True,
    # )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )