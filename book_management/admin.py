from django.contrib import admin

from book_management.models import Book,Category

class BookInline(admin.TabularInline):
    model = Book

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']})
    ]
    search_fields = ['name']   
    list_filter = ['name']
    inlines = [BookInline]
    Category_display = ('name')

admin.site.register(Category, CategoryAdmin)
