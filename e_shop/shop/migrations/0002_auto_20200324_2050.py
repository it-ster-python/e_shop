# Generated by Django 3.0.4 on 2020-03-24 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dresssize',
            options={'verbose_name': 'Dress sizes', 'verbose_name_plural': 'Sezes of dreses'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product for shop', 'verbose_name_plural': 'Products for shop'},
        ),
    ]
