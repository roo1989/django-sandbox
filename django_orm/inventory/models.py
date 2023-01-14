from django.db import models


class Brand(models.Model):
    brand_id = models.BigAutoField(primary_key=True)
    name = models.CharField("Brand Name", max_length=50)

    def __str__(self) -> str:
        return f"Brand name: {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    url = models.SlugField()
    is_active = models.BooleanField()

class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
