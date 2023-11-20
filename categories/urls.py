from django.urls import path

from .views import (
    categories_view, 
    create_category_view, 
    update_category_view,
    delete_category_view,
)

app_name = 'categories'

urlpatterns = [
    path('', categories_view, name='categories'),
    path('create_category/', create_category_view, name='create_category'),
    path('update_category/<int:pk>', update_category_view, name='update_category'),
    path('delete_category/<int:pk>', delete_category_view, name='delete_category'),
]
