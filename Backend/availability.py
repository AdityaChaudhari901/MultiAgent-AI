from utils.google_client import get_calendar_service
from datetime import datetime, timedelta

def check_availability(email, date, start_time, end_time):
    """
    Checks if the user is available between start_time and end_time.
    """
    # Validate time range
    if start_time == end_time:
        return {
            "error": "Start time and end time cannot be the same. Please specify a valid time range."
        }
    
    # Validate start is before end
    try:
        start_dt = datetime.strptime(start_time, "%H:%M")
        end_dt = datetime.strptime(end_time, "%H:%M")
        if start_dt >= end_dt:
            return {
                "error": f"Start time ({start_time}) must be before end time ({end_time})"
            }
    except ValueError:
        return {
            "error": "Invalid time format. Use HH:MM (e.g., 09:00, 14:30)"
        }

    service = get_calendar_service()

    # Combine date + time
    start_datetime = f"{date}T{start_time}:00+05:30"
    end_datetime = f"{date}T{end_time}:00+05:30"

    body = {
        "timeMin": start_datetime,
        "timeMax": end_datetime,
        "items": [{"id": email}]
    }

    response = service.freebusy().query(body=body).execute()
    calendars = response["calendars"]

    busy_slots = calendars[email]["busy"]

    if busy_slots == []:
        return {"available": True, "message": "User is free in this time slot"}
    else:
        return {"available": False, "message": "User is busy in this time slot"}
