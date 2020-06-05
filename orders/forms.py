from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('name','category','slug')
		labels = {'name':"Product",'category':"Category"}







    