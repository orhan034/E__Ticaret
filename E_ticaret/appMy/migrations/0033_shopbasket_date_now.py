# Generated by Django 4.1.5 on 2023-03-22 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0032_alter_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopbasket',
            name='date_now',
            field=models.DateField(null=True, verbose_name='Sepet Tarihi'),
        ),
    ]