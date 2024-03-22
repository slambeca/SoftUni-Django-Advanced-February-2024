from django.contrib import admin

from Petstagram.pets.models import Pet

# admin.site.register(Pet)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_birth", "slug", "pet_photo")