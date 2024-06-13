from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    rating = models.FloatField()
    availability = models.CharField(max_length=20, default='yes')
    company = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='Uncategorized')

    def __str__(self):
        return self.product_name
