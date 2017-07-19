# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-15 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0013_auto_20170712_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppic', models.ImageField(upload_to='ppic/', verbose_name='Profile picture')),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('fb', models.URLField(verbose_name='Facebook')),
                ('ig', models.URLField(verbose_name='Instagram')),
                ('tw', models.URLField(verbose_name='Twitter')),
                ('desc', models.TextField(max_length=3000)),
            ],
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='frontpage',
            field=models.BooleanField(default=False, verbose_name='Display on frontpage?'),
        ),
    ]