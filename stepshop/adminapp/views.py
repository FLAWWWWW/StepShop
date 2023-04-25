from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from authapp.forms import ShopUserRegisterForm, ShopUserEditForm, ProductCategoryEditForm, ProductCategoryRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class UsersListView(ListView):
    model = ShopUser
    template_name = 'admin_staff/users.html'
    context_object_name = 'users_list'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        # context['title'] = 'пользователи'
        context.update({'title': 'пользователи'})
        return context

    def get_queryset(self):
        return ShopUser.objects.order_by('-is_active',
                                            '-is_superuser',
                                            '-is_staff',
                                            'username')


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'admin_staff/create/user_create.html'
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        context.update({'title': 'пользователи | создать'})
        return context


class UserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserEditForm
    template_name = 'admin_staff/update/user_update.html'
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['user_form'] = ShopUserEditForm(instance=self.request.user)
        context.update({'title': 'пользователи | редактировать'})
        return context


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'admin_staff/delete/user_delete.html'
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data()
        context.update({'title': 'пользователи | удаление'})
        return context


class UsersListView(ListView):
    model = ShopUser
    template_name = 'admin_staff/users.html'
    context_object_name = 'users_list'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        # context['title'] = 'пользователи'
        context.update({'title': 'пользователи'})
        return context

    def get_queryset(self):
        return ShopUser.objects.order_by('-is_active',
                                            '-is_superuser',
                                            '-is_staff',
                                            'username')


class CategoriesListView(ListView):
    model = ProductCategory
    template_name = 'admin_staff/categories.html'
    context_object_name = 'categories_list'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesListView, self).get_context_data()
        context.update({'title': 'категории'})
        return context

    def get_queryset(self):
        return ProductCategory.objects.order_by('name')


class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryRegisterForm
    template_name = 'admin_staff/create/category_create.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data()
        context.update({'title': 'категории | создать'})
        return context


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'admin_staff/update/category_update.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['category_form'] = ShopUserEditForm(instance=self.request.user)
        context.update({'title': 'категории | редактировать'})
        return context


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admin_staff/delete/category_delete.html'
    success_url = reverse_lazy('admin_staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data()
        context.update({'title': 'категории | удаление'})
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     title = 'продукты'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     context = {
#         'title': title,
#         'category': category,
#         'products_list': products_list,
#     }
#
#     return render(request, 'admin_staff/products.html', context)
#
#
# def product_create(request, pk):
#     pass
#
#
# def product_read(request, pk):
#     pass
#
#
# def product_update(request, pk):
#     pass
#
#
# def product_delete(request, pk):
#     pass
