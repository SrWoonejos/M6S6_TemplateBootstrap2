from django.urls import path
from .views import list_books

urlpatterns = [
    path('list_books/', list_books, name='list_books'),
]
