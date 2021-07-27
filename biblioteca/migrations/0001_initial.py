# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=40)),
                ('email', models.EmailField(verbose_name='e-mail', max_length=254, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('domicilio', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=40)),
                ('pais', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('portada', models.ImageField(null=True, upload_to='portadas')),
                ('autores', models.ManyToManyField(to='biblioteca.Autor')),
                ('editor', models.ForeignKey(to='biblioteca.Editor')),
            ],
        ),
    ]
