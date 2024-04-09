from django.db import models


class Genre(models.TextChoices):
    Fantasy = "Fantasy"
    ScienceFiction = "Science-Fiction"
    Drama = "Drama"
    Comedy = "Comedy"
    Action = "Action"


class Book(models.Model):
    MAX_LENGTH_TITLE, MAX_LENGTH_AUTHOR = 20, 20
    MAX_LENGTH_DESCRIPTION = 100

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,

    )
    pages = models.IntegerField(
        default=0,
    )

    description = models.TextField(
        max_length=MAX_LENGTH_DESCRIPTION,
        default='',
    )

    author = models.CharField(
        max_length=MAX_LENGTH_AUTHOR,
    )

    genre = models.CharField(
        max_length=max(len(choice) for choice, _ in Genre.choices),
        choices=Genre.choices,
    )