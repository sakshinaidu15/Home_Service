# Generated by Django 4.2.13 on 2024-05-16 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_orders_order_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_data',
            field=models.DateField(auto_created=True, auto_now_add=True, null=True),
        ),
    ]