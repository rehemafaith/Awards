# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-29 09:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awarded', '0002_auto_20190529_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev', models.CharField(blank=True, max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='awarded.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
