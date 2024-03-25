from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, forms as auth_forms, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from Petstagram.accounts.forms import PetstagramUserCreationForm
from Petstagram.accounts.models import PetstagramUser, Profile
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


# def details_profile(request, pk):
#     context = {}
#
#     return render(request, "accounts/details_profile.html", context)


class ProfileDetailsView(views.DetailView):
    queryset = (Profile.objects.
                prefetch_related("user")
                .all())
    template_name = "accounts/details_profile.html"


# def edit_profile(request, pk):
#     context = {}
#
#     return render(request, "accounts/edit_profile.html", context)


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/edit_profile.html"
    fields = ("first_name", "last_name", "date_of_birth", "profile_picture",)

    def get_success_url(self):
        return reverse("details profile", kwargs={
            "pk": self.object.pk,
        })


# def delete_profile(request, pk):
#     context = {}
#
#     return render(request, "accounts/delete_profile.html", context)


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "accounts/delete_profile.html"
    
