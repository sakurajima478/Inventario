from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    home_view,
    about_view,
    register_view,
    login_view,
    logout_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home_view, name='home'),
    path('about', about_view, name='about'),
    
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('categories/', include('categories.urls', namespace='categories')),
    path('products/', include('products.urls', namespace='products')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
