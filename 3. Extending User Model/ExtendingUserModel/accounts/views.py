from django import forms
from django.contrib.auth import views as auth_views, forms as auth_forms, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from ExtendingUserModel.accounts.models import Profile

UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')


class AccountUserCreationForm(auth_forms.UserCreationForm):
    age = forms.IntegerField()
    # Other fields of "Profile"

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        # fields = auth_forms.UserCreationForm.Meta.fields + ("age", )
        fields = (UserModel.USERNAME_FIELD,)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            age=self.cleaned_data["age"],
        )

        if commit:
            profile.save()

        return user


class RegisterUserView(views.CreateView):
    form_class = AccountUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')