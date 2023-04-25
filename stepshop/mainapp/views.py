from random import sample

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product

linkы_menu = [
        {'href': 'index', 'name': 'Главная', 'route': ''},
        {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
        {'href': 'about', 'name': 'О нас', 'route': 'about/'},
        {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    ]


def get_basket(user):
    if user.is_authenticated:
         return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    products = Product.objects.all()
    return sample(list(products), 1)[0]


def get_same_products(product):
    same_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)
    return same_products



def products(request, pk=None):
    title = "продукты/каталог"
    products = Product.objects.all().order_by('-price') #[:2]
    categories = ProductCategory.objects.all()

    paginator = Paginator(products, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    basket = get_basket(request.user)

    context = {
        'title': title,
        'links_menu': linkы_menu,
        'products': products,
        'categories': categories,
        'basket': basket,
        "page_obj": page_obj,
    }

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all()
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_ = Product.objects.filter(category__pk=pk)

        context.update({'products': products_, 'category': category})

    return render(request, 'products.html', context)
    # return render(request = request, template_name='products.html', context=context)


def product(request, pk):
    title = "продукт"

    product_item = get_object_or_404(Product, pk=pk)
    category = product_item.category

    same_products = get_same_products(product_item)
    hot_product = get_hot_product()

    products = Product.objects.all().order_by('-price')  # [:2]
    categories = ProductCategory.objects.all()

    context = {
        'title': title,
        'links_menu': linkы_menu,
        'product': product_item,
        'category': category,
        'products': products,
        'categories': categories,
        'same_products': same_products,
        'hot_product': hot_product,
    }

    return render(request, 'product.html', context)
