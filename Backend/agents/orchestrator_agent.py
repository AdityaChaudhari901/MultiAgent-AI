from typing import Dict, Any, Optional
from agents.availability_agent import AvailabilityAgent
from agents.email_agent import EmailAgent
from agents.scheduler_agent import SchedulerAgent
from utils.gemini_client import parse_intent_with_gemini
import os

availability_agent = AvailabilityAgent()
email_agent = EmailAgent()
scheduler_agent = SchedulerAgent()

def parse_intent(user_text: str) -> Dict[str, Any]:
    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key:
        result = parse_intent_with_gemini(user_text)
        if "error" not in result:
            return result
    return parse_intent_regex(user_text)

def parse_intent_regex(user_text: str) -> Dict[str, Any]:
    text = user_text.lower()
    result = {"intent": None}
    if "schedule" in text or "meeting" in text or "meet" in text:
        result["intent"] = "schedule"
    elif "availability" in text or "available" in text or "free" in text:
        result["intent"] = "check"
    elif "email" in text or "mail" in text:
        result["intent"] = "email"
    else:
        result["intent"] = "schedule"
    import re
    m = re.search(r'[\w\.-]+@[\w\.-]+', user_text)
    if m:
        result["email"] = m.group(0)
    m_date = re.search(r"\d{4}-\d{2}-\d{2}", user_text)
    if m_date:
        result["date"] = m_date.group(0)
    m_time = re.findall(r"([01]?\d|2[0-3]):([0-5]\d)", user_text)
    if m_time:
        result["start_time"] = f"{m_time[0][0]}:{m_time[0][1]}"
        if len(m_time) > 1:
            result["end_time"] = f"{m_time[1][0]}:{m_time[1][1]}"
        else:
            from datetime import datetime, timedelta
            start = datetime.strptime(result["start_time"], "%H:%M")
            end = start + timedelta(hours=1)
            result["end_time"] = end.strftime("%H:%M")
    result.setdefault("start_time", "09:00")
    result.setdefault("end_time", "10:00")
    return result

def run_multi_agent(user_text: str, structured_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    data = structured_data or parse_intent(user_text)
    intent = data.get("intent")
    target_email = data.get("email")
    date = data.get("date")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    subject = data.get("subject", "Meeting Request")
    message = data.get("message", f"Meeting scheduled on {date} at {start_time}.")
    attendees = [target_email] if target_email else []
    response = {"intent": intent, "steps": []}
    if intent == "check":
        if not target_email or not date:
            return {"error": "Missing email/date"}
        availability = availability_agent.run(target_email, date, start_time, end_time)
        response["steps"].append({"availability": availability})
        return response
    if intent == "email":
        if not target_email:
            return {"error": "Missing recipient email"}
        result = email_agent.run(to=target_email, subject=subject, message=message)
        response["steps"].append({"email": result})
        return response
    if intent == "schedule":
        if not target_email or not date:
            return {"error": "Missing email/date"}
        availability = availability_agent.run(target_email, date, start_time, end_time)
        response["steps"].append({"availability": availability})
        if not availability.get("available", False):
            response["result"] = {"status": "busy"}
            return response
        
        # Step 1: Schedule the meeting first to get the meet link
        schedule_result = scheduler_agent.run(
            summary=subject, 
            description=message, 
            date=date, 
            start_time=start_time, 
            end_time=end_time, 
            attendees=attendees
        )
        response["steps"].append({"schedule": schedule_result})
        
        # Step 2: Send email with meeting link included
        template_data = {
            "recipient_name": target_email.split('@')[0].title(), 
            "date": date, 
            "start_time": start_time, 
            "end_time": end_time, 
            "meeting_topic": subject, 
            "meeting_description": message, 
            "meeting_link": schedule_result.get("meetLink", ""),
            "organizer_name": "Multi-Agent Scheduler"
        }
        email_result = email_agent.run(
            to=target_email, 
            subject=subject, 
            message=message, 
            template_type="confirmation", 
            template_data=template_data
        )
        response["steps"].append({"email": email_result})
        
        response["result"] = schedule_result
        return response
    return {"error": "Unknown intent", "data": data}
