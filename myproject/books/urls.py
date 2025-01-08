from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Redirige a la página de inicio
    path('list_books/', views.list_books, name='list_books'),  # Redirige al listado de libros
]
