# Generated by Django 5.0.6 on 2024-06-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpapp', '0002_rename_category_product_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='Uncategorized', max_length=50),
        ),
    ]
