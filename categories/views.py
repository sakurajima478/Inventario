from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import CategoryModel
from products.models import ProductModel
from .forms import CategoryForm

# Create your views here.

@login_required
def categories_view(request):
    categories = CategoryModel.objects.filter(user=request.user)
    return render(request, 'categories/categories.html', {
        'categories' : categories,
    })

@login_required
def products_category_view(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk, user=request.user)
    products_category = ProductModel.objects.filter(user=request.user, category=pk)
    return render(request, 'categories/products_category.html', {
        'category' : category,
        'products' : products_category,
    })

@login_required
def create_category_view(request):
    form = CategoryForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.user = request.user
            new_category.save()
            messages.success(request, 'Category create successfully')
            return redirect('categories:categories')
        
        else:
            messages.warning(request, 'Error data incorrect')
    
    context = {
        'form' : form,
    }
    return render(request, 'categories/create_category.html', context)

@login_required
def update_category_view(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk, user=request.user)
    form = CategoryForm(request.POST or None, instance=category)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully')
            return redirect('categories:categories')
        else:
            messages.warning(request, 'Error data incorrect')
    
    context = {
        'form' : form,
    }
    return render(request, 'categories/update_category.html', context)

@login_required
def delete_category_view(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk, user=request.user)
    category.delete()
    messages.success(request, 'Categrory delete successfully')
    return redirect('categories:categories')