# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-12 16:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import webserver.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileResourceModel',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=webserver.models.report_file_path_generator, validators=[webserver.models.FileResourceValidator()])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImageResourceModel',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=webserver.models.report_file_path_generator)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
