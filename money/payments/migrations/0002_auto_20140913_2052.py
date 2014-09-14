# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDealingQuota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField(verbose_name='\u0421\u0443\u043c\u043c\u0430')),
                ('payment', models.ForeignKey(to='payments.Payment')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='payment',
            name='payers',
            field=models.ManyToManyField(related_name=b'payed_payments', through='payments.PaymentDealingQuota', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
