# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0004_mastbuy'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mastbuy',
            new_name='Mustbuy',
        ),
    ]
