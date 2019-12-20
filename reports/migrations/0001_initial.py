# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-12 16:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import reports.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_public', models.BooleanField(default=False)),
                ('is_accessible', models.BooleanField(default=False)),
                ('authors', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('abstract', models.TextField(blank=True, default='')),
                ('abstract_eng', models.TextField(blank=True, default='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReportFile',
            fields=[
                ('report_file_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('commit_message', models.CharField(blank=True, default='', max_length=1000)),
                ('enabled', models.BooleanField(default=False)),
                ('filename', models.CharField(default='file.pdf', max_length=200)),
                ('file', models.FileField(upload_to=reports.models.report_file_path_generator, validators=[reports.models.ReportFileValidator()])),
                ('report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.Report')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
