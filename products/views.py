from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

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
    if request.method == 'GET':
        form = ProductForm()
        #filters categories that the user created
        form.fields['category'].queryset = CategoryModel.objects.filter(
            user=request.user
        )
        return render(request, 'products/create_product.html', {
            'form': form,
        })
    else:
        try:
            form = ProductForm(request.POST)
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('products:products')
        except ValueError:
            return render(request, 'products/create_product.html', {
            'form': form,
            'error': 'Please data valid',
            })

@login_required
def detail_product_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk, user=request.user)
    return render(request, 'products/detail_product.html', {
        'product' : product,
    })

@login_required
def update_product_view(request, pk):
    if request.method == 'GET':
        product = get_object_or_404(ProductModel, pk=pk, user=request.user)
        form = ProductForm(instance=product)
        form.fields['category'].queryset = CategoryModel.objects.filter(
            user=request.user
        )
        return render(request, 'products/update_product.html', {
            'form' : form,
        })
    else:
        try:
            product = get_object_or_404(ProductModel, pk=pk, user=request.user)
            form = ProductForm(request.POST, instance=product)
            form.save()
            return redirect(f'/products/detail_product/{pk}')
        except ValueError:
            return render(request, 'products/update_product.html', {
                'form' : form,
                'error' : 'Error updating category',
            })

@login_required
def delete_product_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk, user=request.user)
    product.delete()
    return redirect('products:products')