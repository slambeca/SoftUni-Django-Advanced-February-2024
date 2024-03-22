
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import models as auth_models

from Petstagram.accounts.managers import PetstagramUserManager

"""
# Auth in Django

1. Use built-in user - works out of the box (not a good idea)
2. Use built-in user only for auth and define "Profile" model for user data (not the best idea)
3. Define a custom user model for auth and define "Profile" model for user data
"""


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    # password - comes from AbstractBaseUser
    # last_login - comes from AbstractBaseUser

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "email"

    objects = PetstagramUserManager()


class Profile(models.Model):
    MAX_FNAME_LENGTH = 30
    MAX_LNAME_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_FNAME_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LNAME_LENGTH,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
    user = models.OneToOneField(
        PetstagramUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )