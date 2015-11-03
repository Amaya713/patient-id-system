# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edited_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Name', models.CharField(max_length=200)),
                ('DOB', models.CharField(max_length=200)),
                ('Allergies', models.TextField()),
                ('ProcedureName', models.CharField(max_length=200)),
                ('Eye', models.CharField(max_length=2)),
                ('Lens', models.CharField(max_length=200)),
                ('Setfor', models.CharField(max_length=200)),
                ('Lensx', models.CharField(max_length=200)),
                ('Power', models.CharField(max_length=200)),
                ('Comments', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
