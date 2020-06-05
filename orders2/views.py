# coding=utf-8
from django.shortcuts import render, HttpResponse
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.http import HttpResponse
import weasyprint
from django.shortcuts import get_object_or_404
from io import BytesIO
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage

#from .tasks import order_created

@login_required

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            form.user = request.user
            form.save()
            for item in cart:
                OrderItem.objects.create(user=request.user,order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])


            email = ('Order nr. {}'.format(order.id),'messagelll','settings.EMAIL_HOST_USER',[order.email])
            subject = 'Pinnochios Pizza & Subs - Order nr. {}'.format(order.id)
            message = ''
            email = EmailMessage(subject,message,'elena.andresprado@gmail.com',[order.email])
            html = render_to_string('orders2/order2/pdf.html', {'order': order})
            out = BytesIO()
            stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/css/pdf.css')]
            weasyprint.HTML(string=html).write_pdf(out,stylesheets=stylesheets)
            email.attach('order_{}.pdf'.format(order.id),out.getvalue(),'application/pdf')
            email.send()
            # launch asynchronous task
            #order_created.delay(order.id)
            return render(request,
                          'orders2/order2/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders2/order2/create.html',
                  {'cart': cart, 'form': form})

def created_list(request): 
    user = request.user
    my_orders = Order.objects.filter(user=user)
    my_orderitems = OrderItem.objects.filter(user=user)

    return render(request,'orders2/order2/order_detail.html',{'my_orders':my_orders,'user':user,'my_orderitems':my_orderitems,})
def orderitems_list(request, id):
    user = request.user
    my_orderitems = OrderItem.objects.filter(user=user)
    orderitems = get_object_or_404(OrderItem, id=id)
    return render(request,'orders2/order2/created_list2.html',{'orderitems':orderitems,'my_orderitems':my_orderitems,})



def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders2/order2/pdf.html',{'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\"order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/css/pdf.css')])
    return response
