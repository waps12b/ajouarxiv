# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-12 10:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordChangeRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('hashcode', models.CharField(max_length=256, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expired_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
