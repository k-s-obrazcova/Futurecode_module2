from django.urls import path

from .views import *

urlpatterns = [
    path('books/', book_list, name='catalog_book_page'),
    path('books/details/<int:id>/',book_details, name='details_book_page'),
    path('publishing_house/create/', publishing_house_create, name='create_publishing_house_page'),

    path('registration/', user_registration, name='regis'),
    path('login/', user_login, name='log in'),
    path('logout/', user_logout, name='log out'),

    path('anonim/', anonim, name='anonim'),
    path('index/', home, name='home'),
    path('auth/', auth, name='auth'),
    path('add/', add_publishing_house, name='add'),
    path('add_change/', add_change_publishing_house, name='add_change'),
    path('change_only_telephone/', change_only_telephone_publishing_house, name='change_only_telephone'),

]