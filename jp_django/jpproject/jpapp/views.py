from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import Product
import json
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

from django.shortcuts import HttpResponse
import json
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def product_list(request, company=None, category=None):
    top_n = request.query_params.get('top', None)
    min_price = request.query_params.get('MinPrice')
    max_price = request.query_params.get('MaxPrice')
    products = Product.objects.filter(company=company, product_name__icontains=category)
    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)
    if top_n:
        try:
            top_n = int(top_n)
            products = products.order_by('-rating')[:top_n]
        except ValueError:
            pass

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

COMPANIES = ['AMZ', 'FLP', 'SNP', 'MYN', 'AZO']
CATEGORIES = ["Phone", "TV", "SLR", "MPHN", "TABT", "Charger", "Mouse", "Keypad", "Bluetooth", "Pendrive (G)", "Speaker", "Headset", "Laptop", "PC"]



def insert_products(request):
    json_data = '''
    [
      {
        "productName": "Laptop 13",
        "price": 1234.7,
        "discount": 3,
        "rating": 4.5,
        "availability": "yes",
        "company": "AMZ",
        "category": "Laptop"
      },
      {
        "productName": "Laptop 11",
        "price": 1244,
        "rating": 4.5,
        "discount": 45,
        "availability": "out-of-stock",
        "company": "FLP",
        "category": "Laptop"
      },
      {
        "productName": "Laptop 3",
        "price": 9102,
        "rating": 4.44,
        "discount": 98,
        "availability": "out-of-stock",
        "company": "SNP",
        "category": "Laptop"
      },
      {
        "productName": "Laptop 1",
        "price": 2652,
        "rating": 4.12,
        "discount": 70,
        "availability": "yes",
        "company": "MYN",
        "category": "Laptop"
      },
      {
        "productName": "Laptop 4",
        "price": 1258,
        "rating": 3.8,
        "discount": 33,
        "availability": "yes",
        "company": "AZO",
        "category": "Laptop"
      },
      {
        "productName": "Laptop 14",
        "price": 9254,
        "rating": 3,
        "discount": 56,
        "availability": "yes",
        "company": "AMZ",
        "category": "Laptop"
      },
      {
        "productName": "Phone X",
        "price": 899.99,
        "discount": 10,
        "rating": 4.5,
        "availability": "yes",
        "company": "FLP",
        "category": "Phone"
      },
      {
        "productName": "Smart TV 4K",
        "price": 1299.99,
        "discount": 15,
        "rating": 4.8,
        "availability": "yes",
        "company": "SNP",
        "category": "TV"
      },
      {
        "productName": "Digital SLR Camera",
        "price": 1599.95,
        "discount": 5,
        "rating": 4.6,
        "availability": "yes",
        "company": "MYN",
        "category": "SLR"
      },
      {
        "productName": "MPHN Pro Max",
        "price": 1099.95,
        "discount": 8,
        "rating": 4.7,
        "availability": "yes",
        "company": "AZO",
        "category": "MPHN"
      },
      {
        "productName": "Tablet 10.5 inch",
        "price": 499.99,
        "discount": 10,
        "rating": 4.3,
        "availability": "yes",
        "company": "AMZ",
        "category": "TABT"
      },
      {
        "productName": "Ultra-Fast Charger",
        "price": 29.99,
        "discount": 0,
        "rating": 3.9,
        "availability": "yes",
        "company": "FLP",
        "category": "Charger"
      },
      {
        "productName": "Gaming Mouse",
        "price": 59.99,
        "discount": 5,
        "rating": 4.2,
        "availability": "yes",
        "company": "SNP",
        "category": "Mouse"
      },
      {
        "productName": "Mechanical Keypad",
        "price": 79.99,
        "discount": 8,
        "rating": 4.4,
        "availability": "yes",
        "company": "MYN",
        "category": "Keypad"
      },
      {
        "productName": "Bluetooth Earphones",
        "price": 39.99,
        "discount": 0,
        "rating": 4.1,
        "availability": "yes",
        "company": "AZO",
        "category": "Bluetooth"
      }
    ]
    '''

    products = json.loads(json_data)
    for product_data in products:
        product = Product(
            product_name=product_data['productName'],
            price=product_data['price'],
            discount=product_data['discount'],
            rating=product_data['rating'],
            availability=product_data['availability'],
            company=product_data['company'],
            category=product_data['category']
        )
        product.save()

    return HttpResponse("Products inserted successfully.")


@api_view(['GET'])
def api_product_list(request):
    products = Product.objects.all()
    data = list(products.values())
    return Response(data)

def delete(request):
    p=Product.objects.all()
    p.delete()
    return HttpResponse("deleted")
