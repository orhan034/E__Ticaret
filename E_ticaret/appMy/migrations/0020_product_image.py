# Generated by Django 4.1.5 on 2023-03-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0019_alter_product_date_now_alter_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Resim'),
        ),
    ]
