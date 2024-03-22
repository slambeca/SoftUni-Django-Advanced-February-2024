from django.contrib import admin

from Petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ("pk", "location", "tagged_pets", "short_description")

    # @staticmethod
    # def short_description(self, obj):
    #     return obj.description[:5]

    def tagged_pets(self, obj):
        return ", ".join(pet.name for pet in obj.pets.all())

    def short_description(self, obj):
        return obj.description[:6]