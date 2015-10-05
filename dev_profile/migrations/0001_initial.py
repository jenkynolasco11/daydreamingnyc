# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_name', models.CharField(default=b'Daydreaming in NYC', max_length=40)),
                ('page_owner', models.CharField(max_length=20)),
                ('page_message', models.TextField(max_length=500)),
                ('page_message_author', models.CharField(max_length=30)),
                ('page_info', models.TextField(max_length=1000)),
                ('page_photo', models.ImageField(upload_to=b'/home/jenky/Desktop/django-env/jenky/static/image/website_info/')),
            ],
            options={
                'db_table': 'website_info',
                'verbose_name': 'Website Info',
                'verbose_name_plural': 'Website Info',
            },
        ),
    ]
