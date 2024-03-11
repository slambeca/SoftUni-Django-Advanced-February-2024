from django.contrib.auth import views as auth_views, get_user_model
from django.views import generic as views
from django.urls import reverse_lazy


from UserModelAndPasswordManagement.accounts.forms import CreateUserForm

# The correct way to get the "User" class
UserModel = get_user_model()


# authenticate(request, credentials) -> returns the user if credentials match
# login(request, user) -> attaches a cookie for the authenticated user
class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'

    def get_success_url(self):
        return reverse_lazy('index')


class RegisterUserView(views.CreateView):
    # form_class = auth_forms.UserCreationForm
    form_class = CreateUserForm
    template_name = 'accounts/register_user.html'
    success_url = reverse_lazy('index')

# class LoginUserView(views.View):
#     form_class = auth_forms.AuthenticationForm
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': self.form_class()
#         }
#
#         return render(request, 'accounts/login_user.html', context)
#
#     def post(self, request, *args, **kwargs):
#         username, password = request.POST['username'], request.POST['password']
#
#         user = authenticate(username=username, password=password)
#
#         print(user)
#
#         if user is not None:
#             # Add the user to the session
#             login(request, user)
#
#         # login(request, User.objects.get(pk=2))
#
#         return redirect('index')


