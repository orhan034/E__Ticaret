# Generated by Django 4.1.5 on 2023-03-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0023_rename_product_shopbasket_productss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopbasket',
            name='productss',
        ),
        migrations.AddField(
            model_name='shopbasket',
            name='productss',
            field=models.ManyToManyField(to='appMy.product', verbose_name='Ürün'),
        ),
    ]
