# Generated by Django 4.0.3 on 2022-04-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_order_cart_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
