from django.shortcuts import render
from book_management.models import Category, Book

def index(request):
    context = {
        'cat_num': len(Category.objects.all()),
        'book_num' : len(Book.objects.all())
    }
    return render(request, 'index.html', context)