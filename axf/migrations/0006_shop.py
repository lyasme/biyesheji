# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0005_auto_20180404_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
            ],
        ),
    ]
