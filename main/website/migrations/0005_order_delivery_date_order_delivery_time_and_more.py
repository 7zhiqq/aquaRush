# Generated by Django 5.1.4 on 2025-01-10 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_order_created_at_alter_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(max_length=500),
        ),
    ]
