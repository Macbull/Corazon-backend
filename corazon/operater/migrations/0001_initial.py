# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('aadhar_number', models.CharField(unique=True, max_length=13)),
                ('phone_number', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('filename', models.CharField(max_length=10)),
                ('checkup', models.ForeignKey(to='operater.Checkup')),
            ],
        ),
        migrations.AddField(
            model_name='checkup',
            name='patient',
            field=models.ForeignKey(to='operater.Patient'),
        ),
    ]
