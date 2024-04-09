from django.urls import path

from DjangoRESTBasics.apis.views import BookListApiView, BookUpdateApiView

urlpatterns = (
    path('books/', BookListApiView.as_view(), name='api_list_books'),
    path('books/<int:pk>/', BookUpdateApiView.as_view(), name='api_book_update'),
)