from django.contrib import admin

from book_management.models import Book,Category

admin.site.register(Book,Category)