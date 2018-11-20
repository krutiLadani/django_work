# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from Topics.forms import RegisterForm
from Topics.models import Topics, SelectedTopics


def index(request):
    """

    :param request:
    :return:
    """
    return render(request, 'Topics/index.html')


def register(request):
    """

    :param request:
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'], email=form.cleaned_data['email'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'])
            login(request, user)
            return redirect(dashboard)
        else:
            return render(request, 'Topics/register.html', {'form': form})
    form = RegisterForm()
    return render(request, 'Topics/register.html', {'form': form})


@login_required(login_url="login")
def dashboard(request):
    """

    :param request:
    :return:
    """

    user = request.user
    previous_topics = SelectedTopics.objects.filter(selected_by=user,
                                                    selected_on__gte=datetime.now() - timedelta(days=7)) \
        .exclude(selected_on=datetime.now().strftime("%Y-%m-%d")).select_related().order_by('-selected_on').all()
    today_topic = SelectedTopics.objects.filter(selected_by=user,
                                                selected_on=datetime.now().strftime(
                                                    "%Y-%m-%d")).select_related().first()
    context = {"today_topic": today_topic,
               "previous_topics": previous_topics}
    return render(request, 'Topics/dashboard.html', context)


@login_required(login_url="login")
def add_topic(request):
    """

    :param request:
    :return:
    """
    user = request.user
    today_topic = SelectedTopics.objects.filter(selected_by=user,
                                                selected_on=datetime.now().strftime("%Y-%m-%d")).first()
    if not today_topic:
        random_topic = Topics.objects.exclude(selectedtopics__selected_on=datetime.now().strftime("%Y-%m-%d")) \
            .exclude(selectedtopics__selected_by=user.id).order_by("?").first()

        if random_topic:
            new_topic = SelectedTopics(topic_id=random_topic,
                                       selected_by=user,
                                       selected_on=datetime.now().strftime("%Y-%m-%d"))
            new_topic.save()
            messages.add_message(request, messages.INFO, 'Topic selected :) ')
        else:
            messages.add_message(request, messages.INFO, 'All Topics are occupied :( ')
    else:
        messages.add_message(request, messages.INFO, 'Only one topic per day ;) ')
    return redirect(dashboard)
