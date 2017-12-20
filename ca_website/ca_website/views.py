"""Detail views for site."""
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic import TemplateView
from ca_events.models import Meeting
from datetime import datetime


class HomeView(ListView):
    """Display data for splash page."""

    template_name = 'ca_website/home.html'
    context_object_name = 'meetings'
    model = Meeting

    def get_context_data(self, **kwargs):
        """Get specific data needed."""
        today = datetime.now()
        weekday = today.weekday()
        context = super(ListView, self).get_context_data(**kwargs)
        import pdb; pdb.set_trace()


class About(ListView):
    """Display about-ca page."""

    template_name = 'ca_website/about.html'
    context_object_name = 'resources'


class Steps(TemplateView):
    """Display steps and traditions page."""

    template_name = 'ca_website/steps.html'


class Meetings(ListView):
    """Display meeting schedule page."""

    model = Meeting
    template_name = 'ca_website/meeting.html'
    context_object_name = 'meetings'


class EventInfo(ListView):
    """Display Event info page."""

    template_name = 'ca_website/event.html'
    context_object_name = 'events'


class EventDetail(DetailView):
    """Display one event with details."""

    template_name = 'ca_website/event_detail.html'
    context_object_name = 'event'


class AdditionalResources(ListView):
    """Display links to additional resources."""

    template_name = 'ca_website/resource.html'
    context_object_name = 'resources'


def test_view(request):
    """."""
    return render(request, 'ca_website/home.html', {})
