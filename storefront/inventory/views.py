from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Sale, Category
from .forms import SaleForm, ProductForm, CategoryForm

def upload_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category uploaded successfully!')
            return redirect('upload_category')  # Change this to your desired URL after success
    else:
        form = CategoryForm()

    return render(request, 'upload_category.html', {'form': form})

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product uploaded successfully!')
            return redirect('upload_product')  # Change this to your desired URL after success
    else:
        form = ProductForm()

    return render(request, 'upload_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()  # Get all products
    categories = Category.objects.all()  # Get all categories for filtering

    # Filtering logic
    category_filter = request.GET.get('category')
    name_filter = request.GET.get('name')

    if category_filter:
        products = products.filter(category__name=category_filter)

    if name_filter:
        products = products.filter(name__icontains=name_filter)  # Case-insensitive search

    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'category_filter': category_filter,
        'name_filter': name_filter,
    })

# Create your views here.
def create_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Sale recorded successfully!')
                return redirect('create_sale')
            except ValueError as e:
                messages.error(request, str(e))
    else:
        form = SaleForm()

    return render(request, 'create_sale.html', {'form': form})