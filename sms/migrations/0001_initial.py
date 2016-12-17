# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=128)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.House')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.School')),
            ],
        ),
    ]