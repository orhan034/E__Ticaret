# Generated by Django 4.1.5 on 2023-03-19 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0013_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.size', verbose_name='Beden'),
        ),
    ]
