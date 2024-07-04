from .views import *
from .views import *
from django.urls import path, include
urlpatterns = [
    path('product/all/', list_product, name='product_list'),
    path('product/all-filter/', product_list_with_filter, name='product_list_filter'),
    path('product/one-filter/', get_one_filter, name='product_one_filter'),
    path('product/more-filter/', get_more_filter, name='product_more_filter'),
    path('product/detail/<int:id>/', get_one_product, name='get_one_product'),
    # --------------------------- ClassView ------------------------------
    path('supplier/', ListSupplier.as_view(), name='supplier_list'),
    path('supplier/create', CreateSupplier.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/detail/', DetailSupplier.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/update/', UpdateSupplier.as_view(), name='supplier_update'),
    path('supplier/<int:pk>/delete/', DeleteSupplier.as_view(), name='supplier_delete'),
]