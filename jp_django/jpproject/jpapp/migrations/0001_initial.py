# Generated by Django 5.0.6 on 2024-06-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('company', models.CharField(max_length=255)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unique_id', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
