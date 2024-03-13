from django.urls import path

from ExtendingUserModel.accounts.views import LoginUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name="login_user"),
)