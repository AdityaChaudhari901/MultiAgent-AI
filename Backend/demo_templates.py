#!/usr/bin/env python3
"""
Demo script to showcase email templates
"""
from templates.email_templates import get_template
from datetime import datetime, timedelta

def print_template(title: str, template_type: str, data: dict):
    """Print a template example"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")
    
    result = get_template(template_type, data)
    print(f"SUBJECT: {result['subject']}\n")
    print(f"BODY:\n{result['body']}")
    print(f"\n{'='*70}\n")


if __name__ == "__main__":
    # Example data
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    next_week = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    
    print("\n" + "🎨 EMAIL TEMPLATES SHOWCASE".center(70, "="))
    
    # 1. Meeting Invitation
    print_template(
        "1. MEETING INVITATION",
        "invitation",
        {
            "recipient_name": "John",
            "date": tomorrow,
            "start_time": "14:00",
            "end_time": "15:00",
            "meeting_topic": "Project Kickoff",
            "meeting_description": "Discuss project goals and timeline",
            "organizer_name": "Sarah Johnson"
        }
    )
    
    # 2. Meeting Confirmation
    print_template(
        "2. MEETING CONFIRMATION",
        "confirmation",
        {
            "recipient_name": "Alice",
            "date": tomorrow,
            "start_time": "10:00",
            "end_time": "11:00",
            "meeting_topic": "Weekly Sync",
            "organizer_name": "Team Lead"
        }
    )
    
    # 3. Meeting Reminder
    print_template(
        "3. MEETING REMINDER",
        "reminder",
        {
            "recipient_name": "Bob",
            "date": tomorrow,
            "start_time": "16:00",
            "end_time": "17:00",
            "meeting_topic": "Client Presentation",
            "meeting_link": "https://meet.google.com/abc-defg-hij",
            "organizer_name": "Marketing Team"
        }
    )
    
    # 4. Meeting Cancellation
    print_template(
        "4. MEETING CANCELLATION",
        "cancellation",
        {
            "recipient_name": "Charlie",
            "date": tomorrow,
            "start_time": "09:00",
            "meeting_topic": "Budget Review",
            "reason": "urgent client emergency",
            "organizer_name": "Finance Director"
        }
    )
    
    # 5. Meeting Reschedule
    print_template(
        "5. MEETING RESCHEDULE",
        "reschedule",
        {
            "recipient_name": "Diana",
            "old_date": tomorrow,
            "old_start_time": "13:00",
            "new_date": next_week,
            "new_start_time": "14:00",
            "new_end_time": "15:00",
            "meeting_topic": "Strategy Planning",
            "reason": "a scheduling conflict",
            "organizer_name": "CEO Office"
        }
    )
    
    # 6. Availability Check
    print_template(
        "6. AVAILABILITY CHECK",
        "availability",
        {
            "recipient_name": "Eve",
            "date": next_week,
            "start_time": "11:00",
            "end_time": "12:00",
            "meeting_topic": "Design Review",
            "organizer_name": "Product Team"
        }
    )
    
    # 7. Custom Email
    print_template(
        "7. CUSTOM EMAIL",
        "custom",
        {
            "recipient_name": "Frank",
            "subject": "Important Update",
            "message": "I wanted to reach out regarding the upcoming project deadline. Please review the latest documents and provide your feedback by end of week.",
            "organizer_name": "Project Manager"
        }
    )
    
    print("\n✨ All templates generated successfully!\n")
