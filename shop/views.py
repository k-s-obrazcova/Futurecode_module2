from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import ProductFilterForm, SupplierForm
from .models import *
# Create your views here.

def list_product(request):
    list_product = Product.objects.all()
    context = {
        'list_product': list_product
    }
    return render(request, 'shop/product/all_product.html', context)

def product_list_with_filter(request):
    list_product = Product.objects.all()
    if request.GET != None:
        product_form = ProductFilterForm(request.GET)
    else:
        product_form = ProductFilterForm()

    if product_form.is_valid():
        if product_form.cleaned_data.get('name') != "":
            list_product = list_product.filter(name__icontains=product_form.cleaned_data.get('name'))
        if product_form.cleaned_data.get('min_price'):
            list_product = list_product.filter(price__gte=product_form.cleaned_data.get('min_price'))
        if product_form.cleaned_data.get('max_price'):
            list_product = list_product.filter(price__lte=product_form.cleaned_data.get('max_price'))
        context = {
            'list_product': list_product,
            'form': product_form,
        }
        return render(request, 'shop/product/all_filter_product.html', context)



def get_one_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }
    return render(request, 'shop/product/one_product_table.html', context)

def get_one_filter(request):
    find_product = Product.objects.filter(is_exists=request.GET.get('is_ex'))
    context = {
        'list_product': find_product
    }
    return render(request, 'shop/product/all_product.html', context)

def get_more_filter(request):
    find_product = Product.objects.filter(
        price__lte=request.GET.get('max_price'),
        price__gt=request.GET.get('min_price')
    )
    context = {
        'list_product': find_product
    }
    return render(request, 'shop/product/all_product.html', context)




# --------------------------------------- View generic ----------------------
# Набор стандартных CRUD действий
# ListView - Список объектов
# DetailView - Полная информация выбранного объекта
# CreateView - Создать
# UpdateView - Изменить
# DeleteView - Удалить


# class CategoryList(ListView):  # Возврат листа объектов (Категорий)
#
#     # Определяем модель для получения данных
#     model = Category
#     # Установка собственного шаблона
#     # (по умолчанию 'magazine/category_list.html')
#     # (по умолчанию '<название приложения>/<название_модели>_list.html>')
#     template_name = 'magazine/category/category_list.html'
#     # Изменение ключа для передачи данных (object_list)
#     # context_object_name = 'book_list'
#
#     # Доп значения (вторичные/статичные данные)
#     extra_context = {
#         'title': 'Список книг из класса'
#     }
#
#     # Вывод страницы если ни один объект не был найден
#     # True - выводит страницу с пустым списком
#     # False - выводит ошибку 404
#     allow_empty = True
#
#     # Подключение пагинации
#     # С помощью числа выбираем сколько объектов будем выводить на страницу
#     paginate_by = 1
#
#     # Если надо подключить пагинатор для метода
#     # from django.core.paginator import Paginator
#
#     # Доп значение (Динамичные/обрабатываемые данные)
#     # Переопределение метода для добавления доп. данных
#     # К примеру, сюда можно подставить обработку фильтрации
#     def get_context_data(self, *, object_list=None, **kwargs):
#         # Получение имеющихся данных
#         context = super().get_context_data(**kwargs)
#
#         # #
#         # context['title'] = 'Список книг из класса (полученные внутри метода get_context_data)'
#         #
#         # #
#         # context['count_pub'] = publishing_house.objects.all().count()
#         #
#         # # Получение категорий
#         # context['categories'] = category.objects.all()
#         return context
#
#     # Переопределение основного запроса для получения списка объектов
#     def get_queryset(self):
#         return Category.objects.all()  # Запрос по умолчанию

class ListSupplier(ListView):
    model = Supplier
    template_name = 'shop/supplier/supplier_list.html'
    allow_empty = True
    paginate_by = 3


class CreateSupplier(CreateView):
    model = Supplier
    extra_context = {
        'action': 'Создать'
    }
    template_name = 'shop/supplier/supplier_form.html'
    form_class = SupplierForm

class DetailSupplier(DetailView):
    model = Supplier
    template_name = 'shop/supplier/supplier_detail.html'

class UpdateSupplier(UpdateView):
    model = Supplier
    # по умолчанию: название_приложения/название_model + _form.html
    form_class = SupplierForm

    extra_context = {
        'action': 'Изменить'
    }
    template_name = 'shop/supplier/supplier_form.html'

class DeleteSupplier(DeleteView):
    model = Supplier
    # по умолчанию: название_приложения/название_model + _form.html
    template_name = 'shop/supplier/supplier_delete.html'
    success_url = reverse_lazy('product_list_filter')

