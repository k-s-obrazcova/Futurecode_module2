from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Publishing_house)
class Publishing_houseAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Passport_book)
class Passport_bookAdmin(admin.ModelAdmin):
    pass

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'exists')
    list_display_links = ('name',)
    search_fields = ('name', 'price')
    list_editable = ('price', 'exists')
    list_filter = ('exists',)



