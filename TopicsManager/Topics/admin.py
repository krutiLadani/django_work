# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Topics.models import Topics, SelectedTopics

# Register your models here.

admin.site.register(Topics)
admin.site.register(SelectedTopics)
