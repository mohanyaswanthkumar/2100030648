import requests
from django.core.cache import cache

class EcommerceAPI:
    BASE_URL = 'http://testserver/api/companies'
    COMPANIES = ['AMZ', 'FLP', 'SNP', 'MYN', 'AZO']
    CATEGORIES = ["Phone", "TV", "SLR", "MPHN", "TABT", "Charger", "Mouse", "Keypad", "Bluetooth", "Pendrive (G)", "Speaker", "Headset", "Laptop", "PC"]

    def __init__(self):
        self.session = requests.Session()

    def get_products(self, company, category, top, min_price, max_price):
        cache_key = f'products_{company}_{category}_{top}_{min_price}_{max_price}'
        products = cache.get(cache_key)
        if not products:
            url = f'{self.BASE_URL}/{company}/categories/{category}/products'
            params = {'top': top, 'minPrice': min_price, 'maxPrice': max_price}
            response = self.session.get(url, params=params)
            response.raise_for_status()
            products = response.json()
            cache.set(cache_key, products, timeout=60*15)
        return products

    def register(self):
        response = self.session.post(f'{self.BASE_URL}/register')
        response.raise_for_status()
        return response.json()


