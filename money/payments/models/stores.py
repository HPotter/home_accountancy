# *-- coding: utf-8 -*-
from django.db import models


class StoreType(models.Model):
    """
    Store type: restaurant, food store, etc
    """
    name = models.CharField(verbose_name=u"Название", max_length=255)

    def __unicode__(self):
        return self.name


class Store(models.Model):
    """
    Store class: describes stores, restaurants and other places for spending money
    """
    name = models.CharField(verbose_name=u"Название", max_length=255)
    type = models.ForeignKey(StoreType, verbose_name=u"Тип")

    def __unicode__(self):
        return u"[{0}] {1}".format(self.type, self.name)