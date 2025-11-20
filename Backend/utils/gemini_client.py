import os
import json
import google.generativeai as genai
from datetime import datetime, timedelta

# Configure Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def parse_intent_with_gemini(user_text: str) -> dict:
    """
    Use Gemini to parse natural language into structured intent.
    Returns a dict with: intent, email, date, start_time, end_time, subject, message
    """
    if not GEMINI_API_KEY:
        return {"error": "GEMINI_API_KEY not configured"}
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Get current date for relative date parsing
        today = datetime.now()
        current_date_str = today.strftime("%Y-%m-%d")
        current_time_str = today.strftime("%H:%M")
        
        prompt = f"""
You are an AI assistant that extracts structured information from natural language requests about calendar scheduling and emails.

Current date: {current_date_str}
Current time: {current_time_str}

Parse the following user request and return ONLY a JSON object with these fields:
- intent: "schedule" | "check" | "email" (what action the user wants)
- email: email address if mentioned
- date: date in YYYY-MM-DD format (convert "tomorrow", "next week", etc. to actual dates)
- start_time: time in HH:MM 24-hour format (convert "2pm" to "14:00", "morning" to "09:00", etc.)
- end_time: time in HH:MM 24-hour format (default to 1 hour after start_time, but keep it within the same day, max 23:59)
- subject: meeting subject or email subject
- message: meeting description or email message

Rules:
- If "tomorrow" is mentioned, calculate tomorrow's date
- If "next Monday/Tuesday/etc" is mentioned, calculate that date
- If "sunday", "monday" etc. is mentioned without "next", calculate the upcoming occurrence of that day
- Convert times like "2pm", "10:30am", "11pm" to 24-hour format
- For late night meetings (e.g., 11pm), set end_time to 23:59 to keep within same day
- If intent is "schedule" or "meeting", set intent to "schedule"
- If intent is about "availability", "free", "available", set intent to "check"
- If intent is about "email", "mail", "send", set intent to "email"
- Only include fields that are mentioned or can be inferred
- Return ONLY valid JSON, no markdown formatting or explanations

User request: "{user_text}"

JSON response:
"""

        response = model.generate_content(prompt)
        result_text = response.text.strip()
        
        # Clean up markdown code blocks if present
        if result_text.startswith("```json"):
            result_text = result_text[7:]
        if result_text.startswith("```"):
            result_text = result_text[3:]
        if result_text.endswith("```"):
            result_text = result_text[:-3]
        result_text = result_text.strip()
        
        # Parse JSON
        parsed = json.loads(result_text)
        
        # Validate and set defaults
        if "intent" not in parsed:
            parsed["intent"] = "schedule"
        
        # Ensure times are in HH:MM format
        if "start_time" in parsed and "end_time" not in parsed:
            try:
                start = datetime.strptime(parsed["start_time"], "%H:%M")
                end = start + timedelta(hours=1)
                parsed["end_time"] = end.strftime("%H:%M")
            except:
                parsed["end_time"] = "10:00"
        
        # Fix midnight rollover issue: if end_time is "00:00" and start_time is late (e.g., 23:00)
        # then set end_time to "23:59" to keep it within the same day
        if "start_time" in parsed and "end_time" in parsed:
            try:
                start_hour = int(parsed["start_time"].split(":")[0])
                end_hour = int(parsed["end_time"].split(":")[0])
                # If end time is midnight and start is in evening (after 20:00)
                if end_hour == 0 and start_hour >= 20:
                    parsed["end_time"] = "23:59"
            except:
                pass
        
        return parsed
        
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print(f"Response text: {result_text}")
        return {"error": f"Failed to parse Gemini response as JSON: {str(e)}"}
    except Exception as e:
        print(f"Gemini API error: {e}")
        return {"error": f"Gemini API error: {str(e)}"}
