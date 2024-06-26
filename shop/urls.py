from .views import *
from .views import *
from django.urls import path, include
urlpatterns = [
    path('product/all/', list_product, name='product_list'),
    path('product/all-filter/', product_list_with_filter, name='product_list_filter'),
    path('product/one-filter/', get_one_filter, name='product_one_filter'),
    path('product/more-filter/', get_more_filter, name='product_more_filter'),
    path('product/detail/<int:pk>/', get_one_product, name='get_one_product'),


]