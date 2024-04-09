from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("DjangoRESTBasics.web.urls")),
    path("apis/", include('DjangoRESTBasics.apis.urls')),
]


"""
Resource located at /api/books/
Difference between SSR and RESTful APIs

# Server-side rendering

C => POST /api/books/create/ (GET /api/books/create/ for HTML of the form)
R all => GET /api/books/
R details => GET /api/books/2/
U => POST /api/books/update/2/ (GET /api/books/update/ for HTML of the form)
D => POST /api/books/delete/2/ (GET /api/books/delete/ for HTML of the form)

# RESTful API (no need for forms):

C => POST /api/books/
R all => GET /api/books/
R details => GET /api/books/2/
U full => PUT /api/books/
U partial => PATCH /api/books/2/
D => DELETE /api/books/2/

"""