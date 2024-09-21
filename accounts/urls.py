from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    
    path('login', views.login_view,name='login'),
    path('signup', views.signup,name='signup'),
    path('sign_in', views.sign_in,name='sign_in'),
    path('logout', views.logout_view,name='logout'),
    path('login_view', views.login_view,name='login_view'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)