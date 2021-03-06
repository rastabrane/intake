# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-12 22:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0007_add_default_orgs_for_counties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='profiles', to='user_accounts.Organization'),
        ),
    ]
