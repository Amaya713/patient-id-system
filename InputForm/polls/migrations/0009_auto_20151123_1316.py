# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20151123_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Lensx',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Near',
            field=models.CharField(max_length=200, choices=[(b'-1.90', b'-1.90'), (b'-1.25', b'-1.25'), (b'-1.50', b'-1.50'), (b'-1.75', b'-1.75'), (b'-2.00', b'-2.00'), (b'-2.25', b'-2.25'), (b'-2.50', b'-2.50')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ORA',
            field=models.BooleanField(),
        ),
    ]
