# Generated by Django 4.1.5 on 2023-03-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0036_remove_productstok_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product', verbose_name='Resim'),
        ),
    ]
