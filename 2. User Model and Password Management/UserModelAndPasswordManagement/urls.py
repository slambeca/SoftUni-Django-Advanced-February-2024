from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('UserModelAndPasswordManagement.web.urls')),
    path('accounts/', include('UserModelAndPasswordManagement.accounts.urls')),
]
