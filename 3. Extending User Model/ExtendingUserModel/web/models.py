from django.db import models


# No need for database table so it does not inherit models.Model
class AuditModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class Model(AuditModel, models.Model):
    field = models.CharField(
        max_length=20,
    )