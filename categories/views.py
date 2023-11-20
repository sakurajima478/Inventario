from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import CategoryModel
from .forms import CategoryForm

# Create your views here.

@login_required
def categories_view(request):
    categories = CategoryModel.objects.filter(user=request.user)
    return render(request, 'categories/categories.html', {
        'categories' : categories,
    })

@login_required
def create_category_view(request):
    if request.method == 'GET':
        return render(request, 'categories/create_category.html', {
            'form' : CategoryForm,
        })
    else:
        try:
            form = CategoryForm(request.POST)
            new_category = form.save(commit=False)
            new_category.user = request.user
            new_category.save()
            return redirect('categories:categories')
        except ValueError:
            return render(request, 'categories/create_category.html', {
            'form' : CategoryForm,
            'error' : 'please data valid',
            })

@login_required
def update_category_view(request, pk):
    if request.method == 'GET':
        category = get_object_or_404(CategoryModel, pk=pk, user=request.user)
        form = CategoryForm(instance=category)
        return render(request, 'categories/update_category.html', {
            'form' : form,
        })
    else:
        try:
            category = get_object_or_404(CategoryModel, pk=pk, user=request.user)
            form = CategoryForm(request.POST, instance=category)
            form.save()
            return redirect('categories:categories')
        except ValueError:
            return render(request, 'categories/update_category.html', {
                'form' : form,
                'error' : 'Error updating category',
            })

@login_required
def delete_category_view(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk, user=request.user)
    category.delete()
    return redirect('categories:categories')
