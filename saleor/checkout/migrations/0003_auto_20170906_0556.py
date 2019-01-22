# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20170206_0407'),
    ]

    replaces = [
        ('cart', '0003_auto_20170906_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('open', 'Open - currently active'), ('payment', 'Waiting for payment'), ('saved', 'Saved - for items to be purchased later'), ('ordered', 'Submitted - an order was placed'), ('checkout', 'Checkout - processed in checkout'), ('canceled', 'Canceled - canceled by user')], default='open', max_length=32, verbose_name='order status'),
        ),
    ]
