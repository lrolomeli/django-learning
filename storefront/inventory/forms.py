from django import forms
from .models import Sale, Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku', 'name', 'description', 'color', 'category', 'price', 'quantity_in_stock']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity_sold']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']  # Field for category name