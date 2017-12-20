"""Tests for our views."""

from django.test import TestCase
from .views import HomeView, About, Steps, Meetings
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


class StepsTestCase(TestCase):
    """Tests for the Steps view."""

    def setUp(self):
        """Setup for the Steps view."""

    def test_home_view_exists(self):
        """Test that the Steps view exists."""
        response = Steps()
        assert response.template_name == 'ca_website/steps_traditions.html'


class MeetingsTestCase(TestCase):
    """Tests for the Meetings view."""

    def setUp(self):
        """Setup for the Meetings view."""

    def test_home_view_exists(self):
        """Test that the Meetings view exists."""
        response = Meetings()
        assert response.template_name == 'ca_website/meeting.html'


class EventInfoTestCase(TestCase):
    """Tests for the EventInfo view."""

    def setUp(self):
        """Setup for the EventInfo view."""

    def test_home_view_exists(self):
        """Test that the EventInfo view exists."""
        response = EventInfo()
        assert response.template_name == 'ca_website/event.html'


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
        assert response.template_name == 'ca_website/resource.html'
