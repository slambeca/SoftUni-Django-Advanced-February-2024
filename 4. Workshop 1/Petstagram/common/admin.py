from django.contrib import admin

from Petstagram.common.models import PhotoComment


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    pass