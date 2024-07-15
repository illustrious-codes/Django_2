from django.shortcuts import render
from .models import Author, Book

def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    published_date = Book.objects.all()
    context = {
        "authors": authors,
        "books": books,
        "created_at": published_date
    }
    return render(request, 'index.html', context)