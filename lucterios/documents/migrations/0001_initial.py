# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
'''
Initial django functions

@author: Laurent GAY
@organization: sd-libre.fr
@contact: info@sd-libre.fr
@copyright: 2015 sd-libre.fr
@license: This file is part of Lucterios.

Lucterios is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lucterios is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Lucterios.  If not, see <http://www.gnu.org/licenses/>.
'''

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=25)),
                ('description', models.TextField(verbose_name='description')),
                ('modifier', models.ManyToManyField(verbose_name='modifier', blank=True, related_name='category_modifier', to='CORE.LucteriosGroup')),
                ('parent', models.ForeignKey(verbose_name='parent', null=True, to='documents.Category')),
                ('viewer', models.ManyToManyField(verbose_name='viewer', blank=True, related_name='category_viewer', to='CORE.LucteriosGroup')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['parent__name', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=25)),
                ('description', models.TextField(verbose_name='description')),
                ('date_modification', models.DateTimeField(verbose_name='date modification', auto_now_add=True)),
                ('date_creation', models.DateTimeField(verbose_name='date creation', auto_now_add=True)),
                ('category', models.ForeignKey(verbose_name='category', to='documents.Category')),
                ('creator', models.ForeignKey(verbose_name='creator', null=True, to='CORE.LucteriosUser', related_name='document_creator')),
                ('modifier', models.ForeignKey(verbose_name='modifier', null=True, to='CORE.LucteriosUser', related_name='document_modifier')),
            ],
            options={
                'verbose_name_plural': 'document',
                'verbose_name': 'document',
                'ordering': ['category__name', 'name'],
            },
            bases=(models.Model,),
        ),
    ]
