# Generated by Django 4.1.5 on 2023-03-21 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0014_alter_product_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.color', verbose_name='Ürün Rengi'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(to='appMy.size', verbose_name='Ürün Beden'),
        ),
    ]
