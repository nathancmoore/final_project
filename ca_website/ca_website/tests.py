"""Tests for our views."""

from django.test import TestCase
from .views import HomeView, About, Meetings, MeetingDetail
from .views import EventInfo, EventDetail, AdditionalResources
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pdb


class HomeViewTestCase(TestCase):
    """Tests for the HomeView view."""

    def test_home_view_exists(self):
        """Test that the HomeView view exists."""
        response = HomeView()

        assert response.template_name == 'ca_website/home.html'


class AboutTestCase(TestCase):
    """Tests for the About view."""

    def test_home_view_exists(self):
        """Test that the About view exists."""
        response = About()
        assert response.template_name == 'ca_website/about.html'


class MeetingsTestCase(TestCase):
    """Tests for the Meetings view."""

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

    def test_home_view_exists(self):
        """Test that the EventInfo view exists."""
        response = EventInfo()
        assert response.template_name == 'ca_website/events.html'


class EventDetailTestCase(TestCase):
    """Tests for the EventDetail view."""

    def test_home_view_exists(self):
        """Test that the EventDetail view exists."""
        response = EventDetail()
        assert response.template_name == 'ca_website/event_detail.html'

    def test_event_detail_view_context_object(self):
        """Test that the EventDetail context object is correct."""
        response = EventDetail()
        assert response.context_object_name == 'event'


class AdditionalResourcesTestCase(TestCase):
    """Tests for the AdditionalResources view."""

    def test_home_view_exists(self):
        """Test that the AdditionalResources view exists."""
        response = AdditionalResources()
        assert response.template_name == 'ca_website/resources.html'

    def test_all_pdfs_are_present(self):
        """Test that the list of pdfs is complete."""
        response = AdditionalResources()
        assert len(response.pdfs) == 25


class SelTest1(TestCase):
    """."""
    driver = webdriver.Firefox()
    driver.get("http://ec2-34-216-126-115.us-west-2.compute.amazonaws.com/meeting-schedule/")
    cards = driver.find_elements(By.CLASS_NAME, "card-block")
    driver.get("http://ec2-34-216-126-115.us-west-2.compute.amazonaws.com/about-ca/")

    # pdb.set_trace()
    # sunday = driver.find_elements(By.CLASS_NAME, "sunday")[1]
    # monday = driver.find_elements(By.CLASS_NAME, "monday")[1]
    # tuesday = driver.find_elements(By.CLASS_NAME, "tuesday")[1]
    # wednesday = driver.find_elements(By.CLASS_NAME, "wednesday")[1]
    # thursday = driver.find_elements(By.CLASS_NAME, "thursday")[1]
    # friday = driver.find_elements(By.CLASS_NAME, "friday")[1]
    # saturday = driver.find_elements(By.CLASS_NAME, "saturday")[1]

    def test_card_1(self):
        """."""
        assert "Blues Brothers" in self.cards[0].text

    def test_card_2(self):
        """."""
        assert "Wolfpack" in self.cards[1].text

    def test_card_3(self):
        """."""
        assert "The Club House" in self.cards[2].text

    def test_card_4(self):
        """."""
        assert "Good Clean Fun" in self.cards[3].text

    def test_card_5(self):
        """."""
        assert "Blade Runners" in self.cards[4].text

    def test_card_6(self):
        """."""
        assert "New Found Freedom" in self.cards[5].text

    def test_card_7(self):
        """."""
        assert "Recovery Related" in self.cards[6].text

    def test_card_8(self):
        """."""
        assert "Blind Benders" in self.cards[7].text

    def test_number_of_meetings(self):
        """."""
        assert len(self.cards) == 56
