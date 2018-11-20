# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Topics(models.Model):
    """
    Topics model configs
    """
    name = models.CharField(max_length=50)
    pass_code = models.CharField(max_length=50, default="Drc1234")

    def __str__(self):
        return self.name


class SelectedTopics(models.Model):
    """
    Topics model configs
    """
    topic_id = models.ForeignKey(Topics, on_delete=models.CASCADE)
    selected_by = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_on = models.DateField()

    def __str__(self):
        return str(self.topic_id) + "---" + str(self.selected_by) + "---" + str(self.selected_on)
