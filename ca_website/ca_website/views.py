"""Detail views for site."""
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(ListView):
    """Display data for splash page."""
    template_name = 'ca_website/home.html'
    context_object_name = ''


class About(ListView):
    """Display about-ca page."""
    template_name = 'ca_website/about.html'
    context_object_name = ''


class Steps(TemplateView):
    """Display steps and traditions page."""
    template_name = 'ca_website/steps.html'


class Meetings(ListView):
    """Display meeting schedule page."""
    template_name = 'ca_website/meeting.html'
    context_object_name = ''


class Eventinfo(ListView):
    """Display Event info page."""
    template_name = 'ca_website/event.html'
    context_object_name = ''


class Eventdetail(DetailView):
    """Display one event with details."""
    template_name = 'ca_website/event_detail.html'
    context_object_name = ''


class Additional_resources(ListView):
    """Display links to additional resources."""
    template_name = 'ca_website/resource.html'
    context_object_name = ''
