# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class user(models.Model):
    account = models.CharField(max_length=64)
    passwd = models.CharField(max_length=64)
    authority = models.CharField(max_length=64)
    registTime = models.DateTimeField()
