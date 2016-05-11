# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
            ],
            options={
                'verbose_name_plural': 'Favorites',
                'verbose_name': 'Favorite',
            },
        ),
    ]