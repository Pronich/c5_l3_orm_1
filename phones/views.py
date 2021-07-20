from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'min_price':
        items = Phone.objects.all().values('name', 'price', 'slug', 'image').order_by('price')
    elif sort == 'max_price':
        items = Phone.objects.all().values('name', 'price', 'slug', 'image').order_by('-price')
    else:
        items = Phone.objects.all().values('name', 'price', 'slug', 'image').order_by('name')
    phone_lst = []
    for item in items:
        phone = {
            'name': item['name'],
            'price': item['price'],
            'slug': item['slug'],
            'image':item['image']
        }
        phone_lst.append(phone)

    context = {
        'phones': phone_lst
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    item = list(Phone.objects.filter(slug=slug).values())[0]
    context = {
        'phone': {
            'name': item['name'],
            'price': item['price'],
            'release_date': item['release_date'],
            'lte_exists': item['lte_exists'],
            'image': item['image']
        }
    }
    return render(request, template, context)
