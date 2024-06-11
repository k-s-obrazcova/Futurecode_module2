from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import Publishing_houseForm
from .models import *
# Create your views here.

def book_list(request):
    list_books = Books.objects.filter(exists=True)
    context = {
        'list_books': list_books
    }
    return render(request, 'library/books/catalog.html', context)

def book_details(request, id):
    book = get_object_or_404(Books, pk = id)
    context = {
        'book_object': book
    }
    return render(request, 'library/books/details.html', context)

def publishing_house_create(request):
    if request.method == "POST":
        form_publishing_house = Publishing_houseForm(request.POST)
        if form_publishing_house.is_valid():
            new_publishing_house = Publishing_house(**form_publishing_house.cleaned_data)
            new_publishing_house.save()
            return redirect('catalog_book_page')
        else:
            context = {
                'form': form_publishing_house
            }
            return render(request, 'library/publishing_house/create.html', context)
    else:
        form_publishing_house = Publishing_houseForm()
        context = {
            'form': form_publishing_house
        }
        return render(request, 'library/publishing_house/create.html', context)


from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required,permission_required

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RegistrationForm, LoginForm

def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        #form= UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            print(user)

            login(request,user)

            messages.success(request, 'Вы успешно зарегистрировались')

            return redirect('home_page')
        messages.error(request, 'Что-то пошло не так')

    else:
        form = RegistrationForm()
        #form = UserCreationForm()
    return render(request, 'library/auth/registration.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        #form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()

            print('is_anon: ', request.user.is_anonymous)
            print('is_auth: ', request.user.is_authenticated)

            login(request, user)

            print('is_anon: ', request.user.is_anonymous)
            print('is_auth: ', request.user.is_authenticated)
            print(user)

            messages.success(request, 'Вы успешно авторизовались')
            return redirect('home_page')
        messages.error(request, 'Что-то пошло не так')

    else:
        form = LoginForm()
        return render(request,'library/auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.warning(request, 'Вы вышли из аккаунта')
    return redirect('log in')

def anon(request):
    print('is_active: ', request.user.is_active)
    print('is_staff: ', request.user.is_staff)
    print('is_superuser: ', request.user.is_superuser)
    print('is_anonymous: ', request.user.is_anonymous)
    print('is_auth: ', request.user.is_authenticated)

    print('Может ли добавлять поставщика?', request.user.has_perm('magazine.add_supplier'))
    print('Может ли добавлять И изменять поставщика?', request.user.has_perms(['magazine.add_supplier', 'magazine.change_supplier']))
    print('Может ли изменять адрес?', request.user.has_perm('magazine.change_address'))
    return render(request, 'library/test/anon.html')

@login_required()
def auth(request):
    return render(request, 'library/test/auth.html')


@permission_required('magazine.add_supplier')
def can_add_supplier(request):
    return render(request, 'library/test/can_add_supplier.html')

@permission_required(['magazine.add_supplier','magazine.change_supplier'])
def can_change_add_supplier(request):
    return render(request, 'library/test/can_change_add_supplier.html')

@permission_required('magazine.change_address')
def can_change_address(request):
    return render(request, 'library/test/can_change_address.html')


def home(request):
    return render(request, 'library/index.html')