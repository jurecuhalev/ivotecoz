# -*- coding: utf-8 -*-
from django.db import models

ORDER_TYPES = (
    (1, 'Prvi boben'),
    (2, 'Drugi boben'),
    (3, 'Tretji boben'),
    (4, 'Cetrti boben'),
)

class Reel(models.Model):
    order = models.IntegerField(choices=ORDER_TYPES)
    text = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return "%s - %s" % (self.order, self.text)
