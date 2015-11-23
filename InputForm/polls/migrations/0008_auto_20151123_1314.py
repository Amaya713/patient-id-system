# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20151117_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='IStent',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Lensx',
            field=models.CharField(max_length=200, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ORA',
            field=models.CharField(max_length=200, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]
