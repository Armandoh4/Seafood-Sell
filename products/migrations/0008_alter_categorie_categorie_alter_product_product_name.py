# Generated by Django 5.0.6 on 2024-12-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_cart_loged_user_remove_cart_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='categorie',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=30),
        ),
    ]
