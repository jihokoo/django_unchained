# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_1',
            new_name='line_1',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_2',
            new_name='line_2',
        ),
        migrations.AddField(
            model_name='factory',
            name='tags',
            field=models.ManyToManyField(to='utilities.Tag'),
        ),
    ]
