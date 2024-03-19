from django.contrib import admin
from django.urls import path

from DjangoMiddlewaresAndSessions.web.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
]

'''
HTTP (is stateless, each HTTP request is separate:

Client: Sends a request
    Server: Receives a request
        ...
    Server: Sends a response
Client: Receives a response
'''
