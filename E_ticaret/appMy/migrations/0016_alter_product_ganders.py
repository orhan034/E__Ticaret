# Generated by Django 4.1.5 on 2023-03-21 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0015_remove_product_colors_remove_product_sizes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ganders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.gander', verbose_name='Cinsiyet'),
        ),
    ]