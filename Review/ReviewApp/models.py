# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Review(models.Model):
    harshida_review = models.TextField()
    sarang_review = models.TextField()
    chintan_review = models.TextField()
    other_review = models.TextField()
