# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(verbose_name='\u0421\u0443\u043c\u043c\u0430')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0412\u0440\u0435\u043c\u044f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaggedContents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='payments.Payment')),
                ('tag', models.ForeignKey(related_name='payments_taggedcontents_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='store',
            name='type',
            field=models.ForeignKey(verbose_name='\u0422\u0438\u043f', to='payments.StoreType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='contents',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='payments.TaggedContents', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='place',
            field=models.ForeignKey(verbose_name='\u041c\u0435\u0441\u0442\u043e', to='payments.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(verbose_name='\u041f\u043b\u0430\u0442\u0435\u043b\u044c\u0449\u0438\u043a', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
