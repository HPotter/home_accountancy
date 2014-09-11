# *-- coding: utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

from .stores import Store


class TaggedContents(TaggedItemBase):
    content_object = models.ForeignKey('Payment')


class Payment(models.Model):
    """
    Payment class
    """

    user = models.ForeignKey(User, verbose_name=u"Плательщик")
    amount = models.FloatField(verbose_name=u"Сумма")
    date = models.DateTimeField(verbose_name=u"Время", default=datetime.datetime.now)
    place = models.ForeignKey(Store, verbose_name=u"Место")
    contents = TaggableManager(through=TaggedContents)