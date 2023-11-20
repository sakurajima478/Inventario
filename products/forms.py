from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'price', 'stock', 'category']