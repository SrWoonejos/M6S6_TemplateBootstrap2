from django.shortcuts import render
from .models import Book

def list_books(request):
    # Filtrar libros con valoración mayor a 1500
    high_rating_books = Book.objects.filter(rating__gt=1500)
    # Obtener todos los libros
    all_books = Book.objects.all()
    return render(request, 'list_books.html', {
        'high_rating_books': high_rating_books,
        'all_books': all_books,
    })