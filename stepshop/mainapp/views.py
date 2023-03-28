from django.shortcuts import render

from mainapp.models import ProductCategory, Product

linkы_menu = [
        {'href': 'index', 'name': 'Главная', 'route': ''},
        {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
        {'href': 'about', 'name': 'О нас', 'route': 'about/'},
        {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    ]


def products(request):
    title = "продукты/каталог"

    products = Product.objects.all()[:2]
    categories = ProductCategory.objects.all()

    context = {
        'title': title,
        'links_menu': linkы_menu,
        'products': products,
        'categories': categories,
    }

    return render(request, 'products.html', context)
    # return render(request = request, template_name='products.html', context=context)