# Generated by Django 4.1.5 on 2023-03-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0010_productimg_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimg',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Resmin Türü'),
        ),
    ]
