# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 17:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('balanca', '0002_auto_20170929_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesagem',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pesagem',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date da pesagem'),
        ),
    ]
