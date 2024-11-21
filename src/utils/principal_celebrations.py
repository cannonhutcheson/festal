from ics import Calendar, Event
from datetime import datetime, timedelta

# making a new Calendar
calendar = Calendar()

# Adding the principal celebrations for 2025
events = [
    {"name": "First Sunday of Advent", "date":datetime(2024, 12, 1), "desc": "First Sunday of Advent"},
    {"name": "Ash Wednesday", "date":datetime(2025, 3, 5), "desc":"Ash Wednesday, the first day of Lent."},
    {"name": "Easter Sunday", "date":datetime(2025, 4, 20), "desc": "Easter Sunday, Truly He is Risen!"},
    {"name": "The Ascension of the Lord", "date":datetime(2025, 5, 29), "desc":"The Ascention of the Lord"},
    {"name":"Pentecost Sunday", "date":datetime(2025, 6, 8), "desc":"Sunday of Pentecost"},
    {"name":"The Most Holy Body and Blood of Christ", "date":datetime(2025, 6, 22), "desc":"The Most Holy Body and Blood of Christ"},
    {"name": "The First Sunday of Advent", "date":datetime(2025, 11, 30), "desc":"The First Sunday of Advent"}
]

print("Events created")

for info in events:
    event = Event()
    event.name = info["name"]
    event.begin = info["date"]
    event.end = info["date"]
    event.description = info["name"]
    calendar.events.add(event)

print("Events loaded to calendar")

with open('./src/principal_celebrations.ics', 'w') as f:
    f.write(calendar.serialize())