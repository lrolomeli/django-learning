from django.urls import path
from . import views

urlpatterns = [
    path('upload-category/', views.upload_category, name='upload_category'),
    path('upload-product/', views.upload_product, name='upload_product'),
    path('create-sale/', views.create_sale, name='create_sale'),
    path('products/', views.product_list, name='product_list')
]