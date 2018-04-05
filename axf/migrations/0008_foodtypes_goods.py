# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0007_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('typeid', models.CharField(max_length=10)),
                ('typename', models.CharField(max_length=20)),
                ('typesort', models.IntegerField()),
                ('childtypenames', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('productid', models.CharField(max_length=10)),
                ('productimg', models.CharField(max_length=150)),
                ('productname', models.CharField(max_length=50)),
                ('productlongname', models.CharField(max_length=100)),
                ('isxf', models.NullBooleanField(default=False)),
                ('pmdesc', models.CharField(max_length=10)),
                ('specifics', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('marketprice', models.CharField(max_length=10)),
                ('categoryid', models.CharField(max_length=10)),
                ('childcid', models.CharField(max_length=10)),
                ('childcidname', models.CharField(max_length=10)),
                ('dealerid', models.CharField(max_length=10)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
        ),
    ]
