from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'orders2'

urlpatterns = [
    path('admin/orders2/(<int:order_id>/pdf/',views.admin_order_pdf,name='admin_order_pdf'),
	path('', views.order_create, name='order_create'),
	path('list', views.created_list, name='created_list'),
    #path('list/<int:order_id>/', views.order_detail, name='order_detail'),
    path('<int:id>', views.orderitems_list,
         name='orderitems_list'),
	

]
