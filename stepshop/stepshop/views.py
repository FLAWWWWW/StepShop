from django.shortcuts import render

from mainapp.models import ProductCategory, Product

from basketapp.models import Basket

linkы_menu = [
        {'href': 'index', 'name': 'Главная', 'route': ''},
        {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
        {'href': 'about', 'name': 'О нас', 'route': 'about/'},
        {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    ]

def index(request):
    title = "главная"

    products = Product.objects.all()[:2]
    categories = ProductCategory.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'links_menu': linkы_menu,
        'products': products,
        'categories': categories,
        'basket': basket,
    }

    return render(request, 'index.html', context)

def contacts(request):
    title = "контакты"
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'links_menu': linkы_menu,
        'basket': basket,
    }

    return render(request, 'contacts.html', context)

def about(request):
    title = "о нас"

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'links_menu': linkы_menu,
        'basket': basket,
    }

    return render(request, 'about.html', context)