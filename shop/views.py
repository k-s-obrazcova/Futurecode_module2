from types import NoneType

from django.shortcuts import render, redirect

from .forms import ProductFilterForm
from .models import *
# Create your views here.

# def product_list(request):
#     list_product = Product.objects.all()
#     context = {
#         'product_list': list_product
#     }
#     return render(request, 'shop/product/catalog.html', context)

def product_list(request):
    product_list = Product.objects.all()

    # Заполнение формы данными
    if request.GET != None:
        prod_form = ProductFilterForm(request.GET)
    else:
        prod_form = ProductFilterForm()

    # Проверка заполненности данными
    if prod_form.is_valid():

        if prod_form.cleaned_data.get('name') != "":  # строки имеют "" но не пустоту
            product_list = product_list.filter(name__icontains=prod_form.cleaned_data.get('name'))

        if prod_form.cleaned_data.get('max_price'):
            product_list = product_list.filter(price__lte=prod_form.cleaned_data.get('max_price'))

        if prod_form.cleaned_data.get('min_price'):
            product_list = product_list.filter(price__gte=prod_form.cleaned_data.get('min_price'))

    context = {
        'find_product': product_list,
        'form': prod_form,
    }

    return render(request, 'shop/product/catalog.html', context)

def get_one_filter_product(request):
    find_product = Product.objects.filter(is_exists=request.GET.get('is_ex'))
    context = {
        'find_product': find_product
    }
    return render(request, 'shop/product/query_filter_product.html', context)

def get_more_filter_product(request):
    find_product = Product.objects.filter(
        price__lte=request.GET.get('max_price'),
        price__gt=request.GET.get('min_price')
    )
    context = {
        'find_product': find_product
    }
    return render(request, 'shop/product/query_filter_product.html', context)

# def get_more_filter_product(request):
#     max_price = request.GET.get('max_price')
#     min_price = request.GET.get('min_price')
#     if min_price is not None and max_price is not None:
#         if not max_price.isdigit() or not min_price.isdigit():
#             # Обработка ошибки, например, можно вернуть сообщение об ошибке
#             return redirect('product_list')
#         find_product = Product.objects.filter(
#             price__lte=max_price,
#             price__gt=min_price
#         )
#         context = {
#             'find_product': find_product
#         }
#         return render(request, 'shop/product/query_filter_product.html', context)
#     return redirect('product_list')

