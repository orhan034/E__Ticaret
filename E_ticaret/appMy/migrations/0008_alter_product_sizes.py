# Generated by Django 4.1.5 on 2023-03-19 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0007_gander_slug_alter_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.size', verbose_name='Beden'),
        ),
    ]
