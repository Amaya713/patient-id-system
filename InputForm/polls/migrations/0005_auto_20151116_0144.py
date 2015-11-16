# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20151116_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Near',
            field=models.CharField(max_length=200, choices=[(-1.0, b'-1.90'), (-1.25, b'-1.25'), (-1.5, b'-1.50'), (-1.75, b'-1.75'), (-2.0, b'-2.00'), (-2.25, b'-2.25'), (-2.5, b'-2.50')]),
        ),
    ]
