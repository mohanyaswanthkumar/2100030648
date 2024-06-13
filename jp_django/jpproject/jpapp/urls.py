from django.urls import path
from . import views

urlpatterns = [
    path('insert-products/', views.insert_products, name='insert-products'),
    path('product-list/', views.api_product_list, name='api-product-list'),
    path('companies/<str:company>/categories/<str:category>/products/', views.product_list, name='product-list'),
    path('delete',views.delete),
]
