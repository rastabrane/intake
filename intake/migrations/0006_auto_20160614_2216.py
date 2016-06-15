# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 22:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0005_auto_20160606_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationlogentry',
            options={'ordering': ['-time']},
        ),
        migrations.AlterField(
            model_name='applicationlogentry',
            name='submission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logs', to='intake.FormSubmission'),
        ),
        migrations.AlterField(
            model_name='applicationlogentry',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='application_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='old_uuid',
            field=models.CharField(blank=True, max_length=34, unique=True),
        ),
    ]
