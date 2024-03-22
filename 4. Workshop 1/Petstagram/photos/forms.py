from django import forms

from Petstagram.core.form_mixins import ReadOnlyFieldsFormMixin
from Petstagram.photos.models import PetPhoto


class PetPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ("photo", "description", "location", "pets")


class PetPhotoCreateForm(PetPhotoBaseForm):
    pass


class PetPhotoEditForm(ReadOnlyFieldsFormMixin, PetPhotoBaseForm):
    readonly_fields = ("photo", "pets")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["date_of_birth"].widget.attrs["readonly"] = "readonly"
        self._apply_readonly_on_fields()