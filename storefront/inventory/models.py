from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255) # varchar 255

class Product(models.Model):
    COLOR_BRONZE = 'BR'
    COLOR_SILVER = 'SI'
    COLOR_GOLD = 'GO'

    COLOR_CHOICES = [
        (COLOR_BRONZE,'Bronze'),
        (COLOR_SILVER,'Silver'),
        (COLOR_GOLD,'Gold')
    ]
    sku = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255) # varchar 255
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=2, choices=COLOR_CHOICES, default=COLOR_GOLD)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField()  # Available stock quantity

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to Product
    quantity_sold = models.PositiveIntegerField()  # Quantity sold
    sale_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Subtract sold quantity from product stock
        if self.product.quantity_in_stock >= self.quantity_sold:
            self.product.quantity_in_stock -= self.quantity_sold
            self.product.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError('Not enough stock available to fulfill the sale')