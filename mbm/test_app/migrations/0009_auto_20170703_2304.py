# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-03 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0008_imageupload_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(upload_to='user_img/'),
        ),
    ]