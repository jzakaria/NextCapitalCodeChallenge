# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_item_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='due',
            new_name='date',
        ),
    ]
