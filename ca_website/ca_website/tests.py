"""Tests for our views."""

from django.test import TestCase
from .views import HomeView, About, Meetings, MeetingDetail
from .views import EventInfo, EventDetail, AdditionalResources


class HomeViewTestCase(TestCase):
    """Tests for the HomeView view."""

    def setUp(self):
        """Setup for the HomeView view."""

    def test_home_view_exists(self):
        """Test that the HomeView view exists."""
        response = HomeView()

        assert response.template_name == 'ca_website/home.html'


class AboutTestCase(TestCase):
    """Tests for the About view."""

    def setUp(self):
        """Setup for the About view."""

    def test_home_view_exists(self):
        """Test that the About view exists."""
        response = About()
        assert response.template_name == 'ca_website/about.html'


class MeetingsTestCase(TestCase):
    """Tests for the Meetings view."""

    def setUp(self):
        """Setup for the Meetings view."""

    def test_home_view_exists(self):
        """Test that the Meetings view exists."""
        response = Meetings()
        assert response.template_name == 'ca_website/meeting.html'

    def test_home_view_context_object(self):
        """Test that the Meetings context object is correct."""
        response = Meetings()
        assert response.context_object_name == 'meetings'


class MeetingDetailTestCase(TestCase):
    """Tests for the MeetingDetail view."""

    def setUp(self):
        """Setup for the MeetingDetail view."""

    def test_meeting_detail_view_exists(self):
        """Test that the MeetingDetail view exists."""
        response = MeetingDetail()
        assert response.template_name == 'ca_website/meeting_detail.html'

    def test_meeting_detail_view_context_object(self):
        """Test that the MeetingDetail context object is correct."""
        response = MeetingDetail()
        assert response.context_object_name == 'meeting_1'


class EventInfoTestCase(TestCase):
    """Tests for the EventInfo view."""

    def setUp(self):
        """Setup for the EventInfo view."""

    def test_home_view_exists(self):
        """Test that the EventInfo view exists."""
        response = EventInfo()
        assert response.template_name == 'ca_website/events.html'


class EventDetailTestCase(TestCase):
    """Tests for the EventDetail view."""

    def setUp(self):
        """Setup for the EventDetail view."""

    def test_home_view_exists(self):
        """Test that the EventDetail view exists."""
        response = EventDetail()
        assert response.template_name == 'ca_website/event_detail.html'


class AdditionalResourcesTestCase(TestCase):
    """Tests for the AdditionalResources view."""

    def setUp(self):
        """Setup for the AdditionalResources view."""

    def test_home_view_exists(self):
        """Test that the AdditionalResources view exists."""
        response = AdditionalResources()
        assert response.template_name == 'ca_website/resources.html'

    def test_all_pdfs_are_present(self):
        """Test that the list of pdfs is complete."""
        response = AdditionalResources()
        assert len(response.pdfs) == 25
