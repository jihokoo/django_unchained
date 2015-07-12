# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0002_auto_20150708_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='line_2',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='factory',
            name='tags',
            field=models.ManyToManyField(to='utilities.Tag', blank=True),
        ),
    ]
