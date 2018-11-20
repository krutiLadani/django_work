# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
from ReviewApp.forms import ReviewForm


def index(request):
    """

    :param request:
    :return:
    """
    if request.POST:
        form_save = ReviewForm(request.POST)
        form_save.save()
    form = ReviewForm()
    return render(request, 'ReviewApp/index.html', {'form': form})
