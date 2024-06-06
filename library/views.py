from django.shortcuts import render, get_object_or_404, redirect

from library.forms import Publishing_houseForm
from library.models import Books, Publishing_house


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
    return render(request,'library/books/details.html', context)
def publishing_house_create(request):
    if request.method == "POST":
        form_publishing_house = Publishing_houseForm(request.POST)
        if form_publishing_house.is_valid():
            new_supplier = Publishing_house(**form_publishing_house.cleaned_data)
            new_supplier.save()
            return redirect('catalog_publishing_house_page')
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



def publishing_house_list(request):
    list_publishing_house = Publishing_house.objects.all()
    context = {
        'list_publishing_house': list_publishing_house
    }
    return render(request, 'library/publishing_house/catalog.html', context)