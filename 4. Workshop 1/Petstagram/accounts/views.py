from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, forms as auth_forms, login, logout
from django.urls import reverse_lazy
from django.views import generic as views

from Petstagram.accounts.forms import PetstagramUserCreationForm
from Petstagram.accounts.models import PetstagramUser
from Petstagram.pets.models import Pet


# def signup_user(request):
#     context = {}
#
#     return render(request, "accounts/register-page.html", context)


class SignUpUserView(views.CreateView):
    template_name = "accounts/register-page.html"
    form_class = PetstagramUserCreationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        # form_valid will call save
        result = super().form_valid(form)

        login(self.request, form.user)  # or form.instance and no need for save method overriding in the form

        return result


# def signin_user(request):
#     context = {}
#
#     return render(request, "accounts/login-page.html", context)

class SignInUserView(auth_views.LoginView):
    template_name = "accounts/login-page.html"
    redirect_authenticated_user = True


def signout_user(request):
    logout(request)
    return redirect("index")


def details_profile(request, pk):
    context = {
        "pet_photo": Pet.objects.get(pk=pk),
    }

    return render(request, "accounts/details_profile.html", context)


def edit_profile(request, pk):
    context = {}

    return render(request, "accounts/edit_profile.html", context)


def delete_profile(request, pk):
    context = {}

    return render(request, "accounts/delete_profile.html", context)