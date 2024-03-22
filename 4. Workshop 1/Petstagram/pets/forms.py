from django import forms
from django.core.exceptions import ValidationError

from Petstagram.core.form_mixins import ReadOnlyFieldsFormMixin
from Petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet

        fields = ("name", "date_of_birth", "pet_photo")

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Pet name"}),
            "data_of_birth": forms.DateInput(attrs={"type": "date"}),
            "pet_photo": forms.URLInput(attrs={"placeholder": "Link to image"}),
        }

        labels = {
            "name": "Pet name",
            "pet_photo": "Link to image",
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(ReadOnlyFieldsFormMixin, PetBaseForm):
    readonly_fields = ("date_of_birth",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["date_of_birth"].widget.attrs["readonly"] = "readonly"
        self._apply_readonly_on_fields()

    # class Meta:
    #     model = Pet
    #     fields = ("name", "date_of_birth", "pet_photo")

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data["date_of_birth"]
        if date_of_birth != self.instance.date_of_birth:
            raise ValidationError("Date of birth is readonly")

        # return self.instance.date_of_birth
        return date_of_birth


class PetDeleteForm(ReadOnlyFieldsFormMixin, PetBaseForm):
    readonly_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            # self.instance.comment.delete()
            # self.instance.likes.delete()
            self.instance.delete()

        return self.instance()