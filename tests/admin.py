from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from .models import Author, Book, Category


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


class BookAdmin(ImportExportActionModelAdmin):
    pass


# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book, BookAdmin)
