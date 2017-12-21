"""Detail views for site."""
from django.views.generic import ListView, DetailView
# from django.shortcuts import render
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
        import pdb; pdb.set_trace()
        now = today.astimezone(pac)
        weekday = now.strftime('%A')
        context = super(HomeView, self).get_context_data(**kwargs)
        context['meetings'] = Meeting.objects.filter(weekday=weekday)[:3].all()
        context['events'] = Events.objects.filter(published=True).all()
        return context


class About(TemplateView):
    """Display About page."""

    template_name = 'ca_website/about.html'


class Meetings(ListView):
    """Display meeting schedule page."""

    model = Meeting
    template_name = 'ca_website/meeting.html'
    context_object_name = 'meetings'

    def get_context_data(self, **kwargs):
        """."""
        context = super(Meetings, self).get_context_data(**kwargs)
        context['service_meetings'] = ServiceMeeting.objects.all()
        context['sunday_meetings'] = Meeting.objects.filter(weekday="Sunday")
        context['monday_meetings'] = Meeting.objects.filter(weekday="Monday")
        context['tuesday_meetings'] = Meeting.objects.filter(weekday="Tuesday")
        context['wednesday_meetings'] = Meeting.objects.filter(weekday="Wednesday")
        context['thursday_meetings'] = Meeting.objects.filter(weekday="Thursday")
        context['friday_meetings'] = Meeting.objects.filter(weekday="Friday")
        context['saturday_meetings'] = Meeting.objects.filter(weekday="Saturday")
        return context


class EventInfo(ListView):
    """Display Event info page."""

    template_name = 'ca_website/events.html'
    model = Events

    def get_context_data(self, **kwargs):
        """."""
        context = super(EventInfo, self).get_context_data(**kwargs)
        context['events'] = Events.objects.all()
        return context


class AdditionalResources(TemplateView):
    """Display links to additional resources."""

    template_name = 'ca_website/resources.html'
    pdfs = [
        ('What is CA?', '/static/pdf/What_is_CA.pdf'),
        ('Cocaine Anonymous Self-Test', '/static/pdf/Self-Test.pdf'),
        ('To the Newcomer', '/static/pdf/To_the_Newcomer.pdf'),
        ('Too Young to Recover?', '/static/pdf/Too_Young_to_Recover.pdf'),
        ('...And All Other Mind-Altering Substances', '/static/pdf/AAOMAS.pdf'),
        ('Tips for Staying Clean and Sober', '/static/pdf/Tips_for_Staying_Clean_and_Sober.pdf'),
        ('The First 30 Days', '/static/pdf/The_First_30_Days.pdf'),
        ('Anonymity', '/static/pdf/Anonymity.pdf'),
        ('Choosing your Sponsor', '/static/pdf/Choosing_Your_Sponsor.pdf'),
        ('A Guide to the 12 Steps', '/static/pdf/A_Guide_to_the_12_Steps.pdf'),
        ('A Higher Power', '/static/pdf/A_Higher_Power.pdf'),
        ('The Home Group', '/static/pdf/The_Home_Group.pdf'),
        ('Being of Service', '/static/pdf/Being_of_Service.pdf'),
        ('Having Fun in Recovery', '/static/pdf/Having_Fun_in_Recovery.pdf'),
        ('Unity', '/static/pdf/Unity.pdf'),
        ('Crack', '/static/pdf/Crack.pdf'),
        ('Reaching Out to the Deaf and Hard of Hearing', '/static/pdf/Reaching_Out_to_the_Deaf_and_Hard_of_Hearing.pdf'),
        ('CA is Also for the LGBT Addict', '/static/pdf/CA_is_also_for_the_GLBT_Addict.pdf'),
        ('Yes, You Can Start a CA Meeting', '/static/pdf/Yes_You_Can_Start_a_CA_Meeting.pdf'),
        ('Dos and Don\'ts for 12th-Step Calls for Addicts', '/static/pdf/Dos_and_Donts_for_12th_Step_Calls_for_Addicts.pdf'),
        ('A New High from H&I', '/static/pdf/A_New_High_from_HandI.pdf'),
        ('12 Principles', '/static/pdf/12_principles.pdf'),
        ('Tools of Recovery', '/static/pdf/Tools_of_Recovery.pdf'),
        ('WSCA Guidelines', '/static/pdf/20151014_WSCA_Guidelines.pdf'),
        ('WSCA Convention Committee Guidelines', '/static/pdf/WSCA_Convention_Committee_Guidelines.pdf')
    ]

    def get_context_data(self, **kwargs):
        """."""
        context = {}
        context['pdfs'] = self.pdfs
        return context


class MeetingDetail(DetailView):
    """Display all data for a single meeting."""

    model = Meeting
    template_name = 'ca_website/meeting_detail.html'
    context_object_name = 'meeting_1'

    def get_context_data(self, **kwargs):
        """."""
        context = super(MeetingDetail, self).get_context_data(**kwargs)
        return context


class EventDetail(DetailView):
    """Display all data for a single event."""

    model = Events
    template_name = 'ca_website/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        """."""
        context = super(EventDetail, self).get_context_data(**kwargs)
        return context
