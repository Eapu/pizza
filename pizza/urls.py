from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include('account.urls', namespace='account')),
    path("products", include("orders.urls")),
    path('cart', include('cart.urls', namespace='cart')),
    path('orders2', include('orders2.urls', namespace='orders2')),
    path("admin/", admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

