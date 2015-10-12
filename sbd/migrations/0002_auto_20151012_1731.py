# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvr',
            name='art',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tvr',
            name='kol',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tvr',
            name='name',
            field=models.CharField(max_length=300, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tvr',
            name='st',
            field=models.IntegerField(default=0),
        ),
    ]
