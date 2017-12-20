"""Detail views for site."""
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from pytz import timezone
from ca_events.models import Meeting, ServiceMeeting, Events


class HomeView(ListView):
    """Display data for splash page."""

    template_name = 'ca_website/home.html'
    context_object_name = 'meetings'
    model = Meeting

    def get_context_data(self, **kwargs):
        """Get specific data needed."""
        pac = timezone('US/Pacific-New')
        today = datetime.now()
        now = today.astimezone(pac)
        weekday = now.strftime('%A')
        context = super(HomeView, self).get_context_data(**kwargs)
        context['meetings'] = Meeting.objects.filter(weekday=weekday)[:3]
        context['events'] = Events.objects.filter(published=True)
        import pdb; pdb.set_trace()
        return context


class About(ListView):
    """Display about-ca page."""

    template_name = 'ca_website/about.html'
    context_object_name = 'resources'


class Steps(TemplateView):
    """Display steps and traditions page."""

    template_name = 'ca_website/steps_traditions.html'


class Meetings(ListView):
    """Display meeting schedule page."""

    model = Meeting
    template_name = 'ca_website/meeting.html'
    context_object_name = 'meetings'

    def get_context_data(self, **kwargs):
        context = super(Meetings, self).get_context_data(**kwargs)
        context['meeting'] = Meeting.objects.all()
        context['service_meeting'] = ServiceMeeting.objects.all()
        return context


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
