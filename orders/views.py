from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter()
    cart_product_form = CartAddProductForm()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'orders/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug)
    cart_product_form = CartAddProductForm()
    products = Product.objects.filter()
    categories = Category.objects.first()


    return render(request,
                  'orders/product/detail.html',
                  {'product': product,'products':products,'categories':categories,
                   'cart_product_form': cart_product_form})






