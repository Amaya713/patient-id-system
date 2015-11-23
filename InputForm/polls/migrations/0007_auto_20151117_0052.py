# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20151116_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='IStent',
            field=models.CharField(default=False, max_length=200, choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='ORA',
            field=models.CharField(default=False, max_length=200, choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='DOB',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='patient',
            name='SetforDistance',
            field=models.CharField(max_length=200, choices=[(b'Distance', b'Distance'), (b'Near', b'Near')]),
        ),
    ]
