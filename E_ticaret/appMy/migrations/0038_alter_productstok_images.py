# Generated by Django 4.1.5 on 2023-03-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0037_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstok',
            name='images',
            field=models.ManyToManyField(blank=True, to='appMy.productimg', verbose_name='Ürün Fotoğrafları'),
        ),
    ]