# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0009_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('userAccount', models.CharField(max_length=20)),
                ('productid', models.CharField(max_length=10)),
                ('productnum', models.IntegerField()),
                ('productprice', models.CharField(max_length=10)),
                ('isChose', models.BooleanField(default=True)),
                ('productimg', models.CharField(max_length=150)),
                ('productname', models.CharField(max_length=100)),
                ('orderid', models.CharField(max_length=20, default='0')),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('orderid', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=20)),
                ('progress', models.IntegerField()),
            ],
        ),
    ]
