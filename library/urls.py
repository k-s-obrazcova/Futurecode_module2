from django.urls import path, include

from .views import *

urlpatterns = [
    path('books/', book_list, name='catalog_book_page'),
    path('books/details/<int:id>/', book_details, name='details_book_page'),
    path('publishing_house/', publishing_house_list, name='catalog_publishing_house_page'),
    path('publishing_house/create/', publishing_house_create, name='create_publishing_house_page'),

]