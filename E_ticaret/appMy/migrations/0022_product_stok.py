# Generated by Django 4.1.5 on 2023-03-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0021_alter_product_date_now_shopbasket'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stok',
            field=models.IntegerField(null=True, verbose_name='Stok'),
        ),
    ]
