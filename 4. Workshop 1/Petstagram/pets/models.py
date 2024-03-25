from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class Pet(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        blank=False,
        null=False,
    )

    pet_photo = models.URLField(
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,  # Only in the Django app, not in the DB, No need for migrations
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:  # slugify(My Name) -> My-Name
            self.slug = slugify(f"{self.name}-{self.pk}")

        super().save(*args, **kwargs)