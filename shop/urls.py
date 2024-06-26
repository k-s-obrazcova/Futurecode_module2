from django.urls import path

from .views import *
urlpatterns = [
    path('product/one-filter/', get_one_filter_product, name='get_one_filter_product'),
    path('product/all/', product_list, name='product_list'),
    path('product/more-filter/', get_more_filter_product, name='get_more_filter_product'),
    path('product/all-filter/', product_list_with_filter, name='product_filter_page'),
    path('product/detail/<int:id>/', get_one_product, name='get_one_product'),
]