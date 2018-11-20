# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Review(models.Model):
    kruti_review = models.TextField()
    khushi_review = models.TextField()
    payu_review = models.TextField()
    other_review = models.TextField()
