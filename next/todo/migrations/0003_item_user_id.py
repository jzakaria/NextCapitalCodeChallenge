# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_item_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
