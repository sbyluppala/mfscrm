# Generated by Django 2.0.5 on 2018-10-07 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_product_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='charge',
            new_name='p_charge',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pickup_time',
            new_name='p_pickup_time',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='p_product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='p_quantity',
        ),
    ]
