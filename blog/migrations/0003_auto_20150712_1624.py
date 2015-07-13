# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_id1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id1',
            field=models.CharField(default=b'1', max_length=10),
            preserve_default=True,
        ),
    ]
