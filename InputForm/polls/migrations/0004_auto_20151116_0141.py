# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20151115_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Setfor',
            new_name='SetforDistance',
        ),
        migrations.AddField(
            model_name='patient',
            name='Near',
            field=models.CharField(default='-1.00', max_length=200, choices=[(b'-1.00', b'-1.90'), (b'-1.25', b'-1.25'), (b'-1.50', b'-1.50'), (b'-1.75', b'-1.75'), (b'-2.00', b'-2.00'), (b'-2.25', b'-2.25'), (b'-2.50', b'-2.50')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='Eye',
            field=models.CharField(max_length=2, choices=[(b'L', b'left'), (b'R', b'Right')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ProcedureName',
            field=models.CharField(max_length=200, choices=[(b'cs', b'cataract surgery'), (b't', b'trabeculectomy'), (b'cst', b'cataract surgery/trabeculectomy'), (b'a', b'Ahmed Valve'), (b'ce', b'Chalazio excison'), (b'rdr', b'Retinal Detachment repair'), (b'emp', b'Epiretinal Membrane peel'), (b'v', b'vitrectormy')]),
        ),
    ]
