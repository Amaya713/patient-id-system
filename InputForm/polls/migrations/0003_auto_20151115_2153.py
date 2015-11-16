# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20151102_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Name',
            new_name='title',
        ),
    ]
