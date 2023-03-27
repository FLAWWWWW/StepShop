from django.shortcuts import render

from mainapp.models import ProductCategory, Product

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

    context = {
        'title': title,
        'links_menu': linkы_menu,
        'products': products,
        'categories': categories,
    }

    return render(request, 'index.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def contacts(request):
    title = "контакты"

    context = {
        'title': title,
        'links_menu': linkы_menu,
    }

    return render(request, 'contacts.html', context)

def about(request):
    title = "о нас"

    context = {
        'title': title,
        'links_menu': linkы_menu,
    }

    return render(request, 'about.html', context)