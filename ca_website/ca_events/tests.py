"""Tests for our Models."""

from __future__ import unicode_literals
from django.test import TestCase
from .models import Meeting, ServiceMeeting, ExternalResources
import factory
import datetime


class MeetingFactory(factory.django.DjangoModelFactory):
    """Factory for Meeting objects to test."""

    class Meta:
        """Meta class."""

        model = Meeting

    district = 0
    meeting_name = "Test Meeting"
    weekday = "Saturday"
    start_time = "1:00 PM"
    end_time = "2:00 PM"
    location_name = "Test location"
    street = "1234 Sample St"
    suite = "101"
    city = "Seattle"
    zip_code = 99999
    room = "55"
    notes = "These are some notes about the test meeting."
    duration = 60
    meeting_format = "BB, W"
    accessiblility = ""
    last_updated = datetime.datetime.now()


class MeetingTestCase(TestCase):
    """Tests for the Meeting class."""

    def setUp(self):
        """Setup for the Meeting class tests."""
        self.meet = MeetingFactory.create()
        self.meet.save()

    def test_meeting_object_exists(self):
        """Test that the Meeting object exists."""
        meet = Meeting.objects.get(meeting_name='Test Meeting')
        assert meet

    def test_location_attributes(self):
        """Test the Meeting object's location properties."""
        meet = Meeting.objects.get(meeting_name='Test Meeting')
        assert meet.location_name == "Test location"
        assert meet.street == "1234 Sample St"
        assert meet.suite == "101"
        assert meet.city == "Seattle"
        assert meet.zip_code == 99999
        assert meet.room == "55"

    def test_time_attributes(self):
        """Test the Meeting object's time properties."""
        meet = Meeting.objects.get(meeting_name='Test Meeting')
        assert meet.start_time == "1:00 PM"
        assert meet.end_time == "2:00 PM"
        assert isinstance(meet.last_updated, datetime.datetime)

    def test_detail_attributes(self):
        """Test the Meeting object's detail properties."""
        meet = Meeting.objects.get(meeting_name='Test Meeting')
        assert meet.district == 0
        assert meet.weekday == "Saturday"
        assert meet.notes == "These are some notes about the test meeting."
        assert meet.meeting_format == "BB, W"
        assert meet.accessiblility == ""

    def tearDown(self):
        """Delete the test objects when done."""
        Meeting.objects.get(meeting_name="Test Meeting").delete()


class ServiceMeetingFactory(factory.django.DjangoModelFactory):
    """Factory for Meeting objects to test."""

    class Meta:
        """Meta class."""

        model = ServiceMeeting

    meeting_name = "Service Meeting"
    meeting_day = "Monday"
    start_time = "5:00 AM"
    location_name = "Test location"
    street = "222 Walnut Ave"
    suite = "ABC"
    city = "Tacoma"
    zip_code = 77777
    room = "500"
    notes = "These are some sample notes."
    last_updated = datetime.datetime.now()


class ServiceMeetingTestCase(TestCase):
    """Tests for the ServiceMeeting class."""

    def setUp(self):
        """Setup for the ServiceMeeting class tests."""
        self.smeet = MeetingFactory.create()
        self.smeet.save()

    def test_service_meeting_object_exists(self):
        """Test that the ServiceMeeting object exists."""
        smeet = ServiceMeeting.objects.get(meeting_name='Test Service Meeting')
        assert smeet

    def test_location_attributes(self):
        """Test the ServiceMeeting object's location properties."""
        smeet = Meeting.objects.get(meeting_name='Test Meeting')
        assert smeet.location_name == "Test location"
        assert smeet.street == "222 Walnut Ave"
        assert smeet.suite == "ABC"
        assert smeet.city == "Tacoma"
        assert smeet.zip_code == 77777
        assert smeet.room == "500"

    def test_time_attributes(self):
        """Test the Meeting object's time properties."""
        smeet = Meeting.objects.get(meeting_name='Test Service Meeting')
        assert smeet.start_time == "5:00 AM"
        assert isinstance(smeet.last_updated, datetime.datetime)

    def test_detail_attributes(self):
        """Test the ServiceMeeting object's detail properties."""
        smeet = Meeting.objects.get(meeting_name='Test Service Meeting')
        assert smeet.weekday == "Monday"
        assert smeet.notes == "These are some sample notes."

    def tearDown(self):
        """Delete the test objects when done."""
        ServiceMeeting.objects.get(meeting_name="Service Meeting").delete()


class ExternalResourcesFactory(factory.django.DjangoModelFactory):
    """Factory for ExternalResources objects to test."""

    class Meta:
        """Meta class."""

        model = ExternalResources

    name = "Test name"
    description = "Test description"
    # link = models.URLField()


class ExternalResourcesTestCase(TestCase):
    """Tests for the ExternalResources class."""

    def setUp(self):
        """Setup for the ExternalResources class tests."""
        self.er = ExternalResources.create()
        self.er.save()

    def test_service_meeting_object_exists(self):
        """Test that the ExternalResources object exists."""
        er = ExternalResources.objects.get(name='Test name')
        assert er

    def test_location_attributes(self):
        """Test the ExternalResources object's properties."""
        er = Meeting.objects.get(meeting_name='Test Meeting')
        assert er.name == "Test name"
        assert er.street == "222 Walnut Ave"

    def tearDown(self):
        """Delete the test objects when done."""
        Meeting.objects.get(meeting_name="Test Service Meeting").delete()
