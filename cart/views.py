from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from django.views.decorators.http import require_POST
from orders.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm


def cart_add(request, product_id, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter()
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')



def cart_clear(request):
	cart = Cart(request)
	cart.clear()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def cart_detail(request):
	categories = Category.objects.all()
	cart = Cart(request)
	for item in cart:
			item['update_quantity_form'] = CartAddProductForm(
							  initial={'quantity': item['quantity'],
							  'update': True})
	return render(request, 'cart/detail.html', {'cart': cart})



