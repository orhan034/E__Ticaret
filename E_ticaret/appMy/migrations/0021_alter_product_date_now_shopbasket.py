# Generated by Django 4.1.5 on 2023-03-21 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0020_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_now',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Ürün giriş tarihi'),
        ),
        migrations.CreateModel(
            name='ShopBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_all', models.FloatField(default=0, verbose_name='Toplam fiyat')),
                ('count', models.IntegerField(default=0, verbose_name='Adet')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
