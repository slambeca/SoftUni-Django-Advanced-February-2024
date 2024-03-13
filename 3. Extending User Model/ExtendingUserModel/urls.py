from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ExtendingUserModel.web.urls')),
    path('accounts/', include('ExtendingUserModel.accounts.urls')),
]
