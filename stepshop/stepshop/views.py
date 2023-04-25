from random import sample

from django.shortcuts import render

from mainapp.models import ProductCategory, Product

from basketapp.models import Basket

linkы_menu = [
        {'href': 'index', 'name': 'Главная', 'route': ''},
        {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
        {'href': 'about', 'name': 'О нас', 'route': 'about/'},
        {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    ]

def get_hot_product():
    products = Product.objects.all()
    return sample(list(products), 1)[0]

def get_basket(user):
    if user.is_authenticated:
         return Basket.objects.filter(user=user)
    return []

def index(request):
    title = "главная"

    basket = get_basket(request.user)

    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    hot_product = get_hot_product()

    context = {
        'title': title,
        'links_menu': linkы_menu,
        'products': products,
        'categories': categories,
        'basket': basket,
        'hot_product': hot_product,
    }

    return render(request, 'index.html', context)

def contacts(request):
    title = "контакты"
    basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': linkы_menu,
        'basket': basket,
    }

    return render(request, 'contacts.html', context)

def about(request):
    title = "о нас"
    basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': linkы_menu,
        'basket': basket,
    }

    return render(request, 'about.html', context)