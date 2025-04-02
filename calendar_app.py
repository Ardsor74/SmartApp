import calendar
from datetime import datetime
import json

def print_calendar(year, month):
    print(calendar.month(year, month))

def add_event(events, date, event):
    if date in events:
        events[date].append(event)
    else:
        events[date] = [event]

def print_events(events):
    for date, evts in events.items():
        print(f"{date}:")
        for evt in evts:
            print(f"  - {evt}")

def save_events(events, filename="events.json"):
    with open(filename, "w") as file:
        json.dump(events, file)

def load_events(filename="events.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
    now = datetime.now()
    print("Calendar:")
    print_calendar(now.year, now.month)

    events = load_events()
    add_event(events, "2025-04-03", "Doctor's appointment")
    add_event(events, "2025-04-04", "Meeting with Bob")
    print("\nEvents:")
    print_events(events)
    save_events(events)