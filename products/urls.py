from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
# from .views import index
from . import views
print('hello')
urlpatterns = [
    path('', views.index,name='home_page'),
    path('aboutus', views.aboutus,name='aboutus'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)