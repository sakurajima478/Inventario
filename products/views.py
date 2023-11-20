from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import ProductModel
from categories.models import CategoryModel
from .forms import ProductForm

# Create your views here.

@login_required
def products_view(request):
    products = ProductModel.objects.filter(user=request.user)
    return render(request, 'products/products.html', {
        'products' : products,
    })


@login_required
def create_product_view(request):
    form = ProductForm(request.POST or None)
    
    #filters categories that the user created
    form.fields['category'].queryset = CategoryModel.objects.filter(user=request.user)
    
    if request.method == 'POST':
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            messages.success(request, 'Product created succesfully')
            return redirect('products:products')
        else:
            messages.warning(request, 'Error data incorrect')
    
    context = {
        'form' : form,
    }
    return render(request, 'products/create_product.html', context)

@login_required
def detail_product_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk, user=request.user)
    return render(request, 'products/detail_product.html', {
        'product' : product,
    })

@login_required
def update_product_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk, user=request.user)
    form = ProductForm(request.POST or None, instance=product)
    form.fields['category'].queryset = CategoryModel.objects.filter(user=request.user)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Product update succesfully')
            return redirect('products:products')
        else:
            messages.warning(request, 'Error data incorrect')
    
    context = {
        'form' : form,
    }
    return render(request, 'products/update_product.html', context)
    

@login_required
def delete_product_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk, user=request.user)
    product.delete()
    messages.success(request, 'Product delete succesfully')
    return redirect('products:products')