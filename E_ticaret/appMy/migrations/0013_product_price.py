# Generated by Django 4.1.5 on 2023-03-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0012_remove_product_images_remove_productimg_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True, verbose_name='Fiyat'),
        ),
    ]
