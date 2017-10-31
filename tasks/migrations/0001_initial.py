# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 03:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tasks.choices


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='Fecha límite')),
                ('status', models.CharField(choices=[('CREATED', 'creado'), ('IN_PROGESS', 'en progreso'), ('COMPLETED', 'completada')], db_index=True, default='CREATED', max_length=50, verbose_name='Estado'),),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Category', verbose_name='Categoría', related_name='tasks')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Dueño', related_name='tasks')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
