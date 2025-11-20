# main.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from agents.orchestrator_agent import run_multi_agent
from agents.availability_agent import AvailabilityAgent
from agents.email_agent import EmailAgent
from agents.scheduler_agent import SchedulerAgent
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()

app = FastAPI(title="Multi-Agent Scheduler API")

# Allow your frontend origin(s) when developing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

availability_agent = AvailabilityAgent()
email_agent = EmailAgent()
scheduler_agent = SchedulerAgent()

class CheckAvailabilityRequest(BaseModel):
    email: str
    date: str            # yyyy-mm-dd
    start_time: str      # HH:MM
    end_time: str        # HH:MM

class SendMailRequest(BaseModel):
    to: str
    subject: str
    message: str

class ScheduleRequest(BaseModel):
    summary: str
    description: Optional[str] = ""
    date: str
    start_time: str
    end_time: str
    attendees: List[str]

class MultiAgentRequest(BaseModel):
    user_text: Optional[str] = None
    structured: Optional[Dict[str, Any]] = None

@app.post("/check-availability")
def check_availability_endpoint(req: CheckAvailabilityRequest):
    try:
        return availability_agent.run(req.email, req.date, req.start_time, req.end_time)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/send-mail")
def send_mail_endpoint(req: SendMailRequest):
    try:
        return email_agent.run(req.to, req.subject, req.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/schedule-meeting")
def schedule_meeting_endpoint(req: ScheduleRequest):
    try:
        return scheduler_agent.run(req.summary, req.description, req.date, req.start_time, req.end_time, req.attendees)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/multi-agent")
def multi_agent_endpoint(req: MultiAgentRequest):
    """
    Accepts either a natural language string in `user_text` or structured JSON in `structured`.
    Example structured for scheduling:
    {
      "intent": "schedule",
      "email": "bob@example.com",
      "date": "2025-11-20",
      "start_time": "11:00",
      "end_time": "12:00",
      "subject": "Quick sync",
      "message": "Let's sync"
    }
    """
    try:
        user_text = req.user_text or ""
        structured = req.structured
        return run_multi_agent(user_text=user_text, structured_data=structured)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
