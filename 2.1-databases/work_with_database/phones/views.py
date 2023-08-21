from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    name = request.GET.get('sort')
    min_price = request.GET.get('sort', 0) 
    max_price = request.GET.get('sort', 0) 
    if min_price == 'min_price':
        phones = phones.order_by('price')
    if max_price == 'max_price':
        phones = phones.order_by('-price')
    if name == 'name':
        phones = phones.order_by('name')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug__icontains=slug)
    context = {'phone': phone}
    return render(request, template, context)
