from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product

linkы_menu = [
        {'href': 'index', 'name': 'Главная', 'route': ''},
        {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
        {'href': 'about', 'name': 'О нас', 'route': 'about/'},
        {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    ]


def products(request):
    title = "продукты/каталог"

    products = Product.objects.all().order_by('-price') #[:2]
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

    return render(request, 'products.html', context)
    # return render(request = request, template_name='products.html', context=context)

def product(request, pk):
    title = "продукт"

    product_item = get_object_or_404(Product, pk=pk)
    category = product_item.category
    products = Product.objects.all().order_by('-price')  # [:2]
    categories = ProductCategory.objects.all()

    context = {
        'title': title,
        'links_menu': linkы_menu,
        'product': product_item,
        'category': category,
        'products': products,
        'categories': categories,
    }

    return render(request, 'product.html', context)
