"""Detail views for site."""
from django.views.generic import ListView, DetailView
from django.views import view


class HomeView(ListView):
    """Display data for splash page."""

    template_name = 'ca_website/home.html'
    context_object_name = 'meetings'


class About(ListView):
    """Display about-ca page."""

    template_name = 'ca_website/about.html'
    context_object_name = 'resources'


class Steps(view):
    """Display steps and traditions page."""

    template_name = 'ca_website/steps.html'


class Meetings(ListView):
    """Display meeting schedule page."""

    template_name = 'ca_website/meeting.html'
    context_object_name = 'meetings'


class Eventinfo(ListView):
    """Display Event info page."""

    template_name = 'ca_website/event.html'
    context_object_name = 'events'


class Eventdetail(DetailView):
    """Display one event with details."""

    template_name = 'ca_website/event_detail.html'
    context_object_name = 'event'


class Additionalresources(ListView):
    """Display links to additional resources."""

    template_name = 'ca_website/resource.html'
    context_object_name = 'resources'
