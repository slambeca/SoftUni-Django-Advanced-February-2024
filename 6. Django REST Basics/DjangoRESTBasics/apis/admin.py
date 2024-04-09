from django.contrib import admin

from DjangoRESTBasics.apis.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre',)