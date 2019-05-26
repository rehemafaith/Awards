# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-26 16:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpg', null=True, upload_to='avatars/')),
                ('bio', models.TextField(max_length=140, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=140)),
                ('img', models.ImageField(upload_to='projects/')),
                ('link', models.CharField(max_length=140)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awarded.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(default='', max_length=140)),
                ('design', models.IntegerField(default=0)),
                ('usability', models.IntegerField(default=0)),
                ('content', models.IntegerField(default=0)),
                ('rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awarded.Project')),
                ('rated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awarded.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Techused',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techused', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='techused',
            field=models.ManyToManyField(to='awarded.Techused'),
        ),
    ]
