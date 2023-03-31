from django.shortcuts import render

# Create your views here.
from .models import Product
from .forms import RawProductForm

def product_create_view(request):
    my_form=RawProductForm()
    if request.method=='POST':
        my_form=RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)
    context={
        'form':my_form
    }
    print(request.GET)
    print(request.POST)
    return render(request, 'products/products_create.html', context)