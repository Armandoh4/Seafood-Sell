from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
# from .views import index
from . import views
print('hello')
urlpatterns = [
    path('', views.index,name='home_page'),
    path('aboutus', views.aboutus,name='aboutus'),
    path('cart', views.cart,name='cart'),
    path('addtocart/<int:id>',views.addtocart,name="addtocart"),
    path('remove/<int:id>',views.removefromcart,name="remove"),
    path('checkout', views.checkout,name='checkout'),
    path('create-checkout-session/', views.checkoutpro, name='create-checkout-session'),
    path('stripe-webhook/', views.stripe_webhook, name='stripe-webhook'),
    path('success', views.success,name='success'),
    path('cancel', views.cancel,name='cancel'),
    path('detail/<int:id>', views.detail,name='detail'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)