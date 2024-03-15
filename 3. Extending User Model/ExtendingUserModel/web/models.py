from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# No need for database table so it does not inherit models.Model
# class AuditModel(models.Model):
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#     )
#     updated_at = models.DateTimeField(
#         auto_now=True,
#     )
#
#     class Meta:
#         abstract = True


# class Model(AuditModel, models.Model):
#     field = models.CharField(
#         max_length=20,
#     )


class Model(models.Model):
    field = models.CharField(
        max_length=20,
    )

    # Do this
    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )
    # We will make a query: request.user.model_set() -> Here we have 1 JOIN

    # Not this
    # profile = models.ForeignKey(
    #     Profile,
    #     on_delete=models.DO_NOTHING,
    # )
    # We will make a query: request.user.profile.model_set() -> Here we have 2 JOINs