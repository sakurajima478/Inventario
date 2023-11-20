from django.urls import path

from .views import (
    products_view,
    create_product_view,
    detail_product_view,
    update_product_view,
    delete_product_view,
)

app_name = 'products'

urlpatterns = [
    path('', products_view, name='products'),
    path('create_product/', create_product_view, name='create_product'),
    path('detail_product/<int:pk>', detail_product_view, name='detail_product'),
    path('update_product/<int:pk>', update_product_view, name='update_product'),
    path('delete_product/<int:pk>', delete_product_view, name='delete_product'),
]
