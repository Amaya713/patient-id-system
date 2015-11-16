# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20151116_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Lensx',
            field=models.CharField(max_length=200, choices=[(True, b'Yes'), (False, b'No')]),
        ),
    ]
