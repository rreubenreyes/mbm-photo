# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-30 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_auto_20170630_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='user_img/')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageUploads',
        ),
    ]
