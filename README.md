# Multi-Agent AI Scheduler

An intelligent multi-agent system for scheduling meetings with natural language processing powered by Google Gemini AI.

## 🌟 Features

- **Natural Language Understanding**: Use Gemini AI to parse natural language requests like "schedule a meeting with john@example.com tomorrow at 2pm"
- **Multi-Agent Architecture**: Specialized agents for availability checking, email sending, and meeting scheduling
- **Google Calendar Integration**: Automatic calendar event creation with Google Meet links
- **Gmail Integration**: Send professional email notifications with beautiful templates
- **Professional Email Templates**: 7 pre-built templates (invitation, confirmation, reminder, cancellation, reschedule, availability check, custom)
- **React Frontend**: User-friendly interface to interact with all agents
- **Smart Time Parsing**: Understands relative dates like "tomorrow", "next Monday", "in 5 minutes"

## 🏗️ Architecture

### Backend (Python + FastAPI)
- **Orchestrator Agent**: Coordinates all agents and parses user intent
- **Availability Agent**: Checks Google Calendar free/busy status
- **Email Agent**: Sends emails via Gmail API with template support
- **Scheduler Agent**: Creates calendar events with Google Meet links
- **Gemini Client**: Natural language processing with fallback to regex

### Frontend (React + Vite)
- Clean UI for testing all agent functions
- Multi-agent workflow interface
- Real-time response display

## 📋 Prerequisites

- Python 3.13+
- Node.js 18+
- Google Cloud Project with Calendar API and Gmail API enabled
- Google OAuth credentials (`credentials.json`)
- Gemini API key

## 🚀 Setup

### Backend Setup

1. Navigate to the Backend directory:
```bash
cd Backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

4. Add your Google OAuth credentials as `credentials.json` in the Backend folder

5. Run the server:
```bash
python3 -m uvicorn main:app --reload --port 8000
```

### Frontend Setup

1. Navigate to the Frontend directory:
```bash
cd Frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

4. Open http://localhost:5173 in your browser

## 🎯 API Endpoints

### POST `/multi-agent`
Natural language multi-agent workflow
```json
{
  "user_text": "schedule a meeting with bob@example.com tomorrow at 2pm"
}
```

### POST `/check-availability`
Check calendar availability
```json
{
  "email": "user@example.com",
  "date": "2025-11-21",
  "start_time": "14:00",
  "end_time": "15:00"
}
```

### POST `/send-mail`
Send email
```json
{
  "to": "recipient@example.com",
  "subject": "Meeting Invitation",
  "message": "Let's meet tomorrow"
}
```

### POST `/schedule-meeting`
Schedule a meeting
```json
{
  "summary": "Team Sync",
  "description": "Weekly team meeting",
  "date": "2025-11-21",
  "start_time": "14:00",
  "end_time": "15:00",
  "attendees": ["member@example.com"]
}
```

## 📧 Email Templates

Available templates:
- `invitation` - Professional meeting invitations
- `confirmation` - Meeting confirmation with Google Meet link
- `reminder` - Meeting reminders
- `cancellation` - Meeting cancellations
- `reschedule` - Meeting rescheduling
- `availability` - Availability check requests
- `custom` - Custom messages

## 🤖 Natural Language Examples

- "Schedule a meeting with john@example.com tomorrow at 2pm"
- "Check if I'm free next Monday at 3pm"
- "Schedule a call with sarah@example.com on Friday at 10am"
- "Meeting with bob@example.com in 30 minutes"
- "Check availability for meeting on Sunday at 11pm"

## 🛠️ Tech Stack

**Backend:**
- FastAPI
- Python 3.13
- Google Gemini AI (gemini-2.0-flash)
- Google Calendar API
- Gmail API
- Uvicorn

**Frontend:**
- React 18
- Vite
- Axios
- CSS3

## 📝 License

MIT License

## 👤 Author

Aditya Chaudhari

## 🙏 Acknowledgments

- Google Gemini AI for natural language processing
- Google Calendar & Gmail APIs for integration
- FastAPI for the backend framework
