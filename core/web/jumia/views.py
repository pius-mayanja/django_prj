from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Product,Categories
from .models import Product

def index(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    return render(request, 'core/index.html', {'products':products,
                                              'categories': categories})

def detail(request, id):
    item = get_object_or_404(Product, pk=id)
    related_items = Product.objects.filter(Category = item.Category).exclude(pk=id)
    return render(request, 'core\detail.html', {'item':item,'related_items':related_items})

