from django.db import models
from django.contrib.auth.models import User



class Categories(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name',]
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    Category = models.ForeignKey(Categories, related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits = 30, decimal_places=2)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    product_by = models.ForeignKey(User, related_name = 'items', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    