from utils.google_client import get_calendar_service
from datetime import datetime

def schedule_meeting(summary, description, date, start_time, end_time, attendees):
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

    event = {
        "summary": summary,
        "description": description,
        "start": {
            "dateTime": f"{date}T{start_time}:00+05:30",
            "timeZone": "Asia/Kolkata",
        },
        "end": {
            "dateTime": f"{date}T{end_time}:00+05:30",
            "timeZone": "Asia/Kolkata",
        },
        "attendees": [{"email": email} for email in attendees],
        "conferenceData": {
            "createRequest": {
                "requestId": f"{summary}-{date}-{start_time}",
                "conferenceSolutionKey": {"type": "hangoutsMeet"}
            }
        }
    }

    created_event = service.events().insert(
        calendarId="primary", 
        body=event,
        conferenceDataVersion=1  # Required to create Google Meet link
    ).execute()
    
    # Extract meeting links
    meet_link = None
    if "conferenceData" in created_event and "entryPoints" in created_event["conferenceData"]:
        for entry in created_event["conferenceData"]["entryPoints"]:
            if entry["entryPointType"] == "video":
                meet_link = entry["uri"]
                break
    
    return {
        "status": "Meeting Scheduled",
        "event_id": created_event.get("id"),
        "htmlLink": created_event.get("htmlLink"),
        "meetLink": meet_link,
        "summary": summary,
        "date": date,
        "start_time": start_time,
        "end_time": end_time
    }
