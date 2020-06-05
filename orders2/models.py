from django.db import models
from orders.models import Product
from account.models import Profile
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders',null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True,null=True,blank=True)
    paid = models.NullBooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    #def get_absolute_url(self):
            #return reverse('orders2:order_detail',
                           #args=[self.id])

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orderitems',null=True,blank=True)
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        index_together = (('id'),)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
