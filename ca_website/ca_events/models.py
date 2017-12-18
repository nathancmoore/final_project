from django.db import models
from multiselectfield import MultiSelectField
import weekday_field


# Create your models here.
class Meeting(models.Model):
    """Meeting model for ca site."""
    district = models.IntegerField(max_lenght=2)
    meeting_name = models.Charfield(max_lenght=50)
    weekday = weekday_field.fields.WeekdayField()
    time = models.DateTimeField()
    end_time = models.DateTimeField()
    location_name = models.Charfield(max_lenght=150)
    street = models.Charfield(max_lenght=250)
    suite = models.Charfield(max_lenght=150)
    city = models.Charfield(max_lenght=150)
    state = models.Charfield(max_lenght=150)
    zip_code = models.IntegerField(max_lenght=15)
    room = models.Charfield(max_lenght=100)
    notes = models.TextField()
    duration = models.Charfield(max_lenght=200)
    meeting_format_choices = [
        ('BB', 'Big Book Study'),
        ('C', 'Closed meeting for those who disire to stop using cocaine and all other substances. Newcommers welcome.'),
        ('CL', 'Candle Light'),
        ('LS', 'Literature Study'),
        ('M', 'Mend only'),
        ('NC', 'No children please.'),
        ('SB', 'Non smoking with break.'),
        ('W', 'Women only.'),
        ('HC', 'Wheelchair accessible'),
    ]
    meeting_format = models.MultiSelectField(
        max_lenght=200,
        choices=meeting_format_choices,
    )
    accessiblility = models.Charfield(max_lenght=150)
    last_updated = models.DateTimeField(auto_now=True)



# {
#     "District": 3,
#     "Meeting_Name": "Kenmore Keystone",
#     "Weekday": "Monday",
#     "Time": "7:30 PM",
#     "End_Time": "8:30 PM",
#     "Location_Name": "Church of the Redeemer",
#     "Street": "6211 NE 182nd St",
#     "Suite": "",
#     "City": "Kenmore",
#     "State": "WA",
#     "Zip": 98029,
#     "Room": "",
#     "Notes": "",
#     "Duration": 60,
#     "Format": "CL, MM",
#     "Accessibility": "",
#     "Updated": "",
# },