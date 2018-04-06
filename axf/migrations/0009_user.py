# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0008_foodtypes_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('userAccount', models.CharField(max_length=20, unique=True)),
                ('userPasswd', models.CharField(max_length=20)),
                ('userName', models.CharField(max_length=20)),
                ('userPhone', models.CharField(max_length=20)),
                ('userAdderss', models.CharField(max_length=100)),
                ('userImg', models.CharField(max_length=150)),
                ('userRank', models.IntegerField()),
                ('userToken', models.CharField(max_length=50)),
            ],
        ),
    ]
