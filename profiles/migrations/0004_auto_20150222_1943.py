# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(max_length=1200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default=b'my location', max_length=1200),
            preserve_default=True,
        ),
    ]
