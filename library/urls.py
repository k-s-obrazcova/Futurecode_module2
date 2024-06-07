from django.urls import path

from .views import *
urlpatterns = [
    path('books/', book_list, name='catalog_book_page'),
    path('books/details/<int:id>/', book_details, name='details_book_page'),
    path('publishing_house/create/', publishing_house_create, name='create_publishing_house_page'),

]