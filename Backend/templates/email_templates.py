"""
Email templates for different types of communications
"""
from datetime import datetime
from typing import Dict, Any


class EmailTemplates:
    """Collection of professional email templates"""
    
    @staticmethod
    def format_date(date_str: str) -> str:
        """Format date string to readable format"""
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj.strftime("%A, %B %d, %Y")
        except:
            return date_str
    
    @staticmethod
    def format_time(time_str: str) -> str:
        """Format time string to readable format"""
        try:
            time_obj = datetime.strptime(time_str, "%H:%M")
            return time_obj.strftime("%I:%M %p")
        except:
            return time_str
    
    @staticmethod
    def meeting_invitation(data: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate a professional meeting invitation email
        
        Args:
            data: Dict with keys: recipient_name, date, start_time, end_time, 
                  meeting_topic, meeting_description, organizer_name
        
        Returns:
            Dict with 'subject' and 'body' keys
        """
        recipient_name = data.get("recipient_name", "there")
        date = data.get("date", "")
        start_time = data.get("start_time", "")
        end_time = data.get("end_time", "")
        topic = data.get("meeting_topic", "Meeting")
        description = data.get("meeting_description", "")
        organizer = data.get("organizer_name", "The Team")
        
        formatted_date = EmailTemplates.format_date(date)
        formatted_start = EmailTemplates.format_time(start_time)
        formatted_end = EmailTemplates.format_time(end_time)
        
        subject = f"Meeting Invitation: {topic}"
        
        body = f"""Hi {recipient_name},

I hope this email finds you well.

I would like to invite you to a meeting to discuss {topic}.

📅 Meeting Details:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Date: {formatted_date}
• Time: {formatted_start} - {formatted_end}
• Topic: {topic}
"""
        
        if description:
            body += f"• Description: {description}\n"
        
        body += """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Please let me know if this time works for you or if you need to reschedule.

Looking forward to meeting with you.

Best regards,
{organizer}

---
This meeting was scheduled via Multi-Agent Scheduler
"""
        
        return {
            "subject": subject,
            "body": body.format(organizer=organizer)
        }
    
    @staticmethod
    def meeting_confirmation(data: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate a meeting confirmation email
        
        Args:
            data: Dict with keys: recipient_name, date, start_time, end_time, 
                  meeting_topic, organizer_name
        
        Returns:
            Dict with 'subject' and 'body' keys
        """
        recipient_name = data.get("recipient_name", "there")
        date = data.get("date", "")
        start_time = data.get("start_time", "")
        end_time = data.get("end_time", "")
        topic = data.get("meeting_topic", "Meeting")
        meeting_link = data.get("meeting_link", "")
        organizer = data.get("organizer_name", "The Team")
        
        formatted_date = EmailTemplates.format_date(date)
        formatted_start = EmailTemplates.format_time(start_time)
        formatted_end = EmailTemplates.format_time(end_time)
        
        subject = f"✓ Meeting Confirmed: {topic}"
        
        body = f"""Hi {recipient_name},

This is to confirm that your meeting has been successfully scheduled.

✓ CONFIRMED MEETING DETAILS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Date: {formatted_date}
• Time: {formatted_start} - {formatted_end}
• Topic: {topic}
• Status: Confirmed ✓
"""
        
        if meeting_link:
            body += f"• 🔗 Join Meeting: {meeting_link}\n"
        
        body += """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A calendar invitation has been sent to your email. Please check your calendar.

If you need to make any changes, please let me know as soon as possible.

Best regards,
{organizer}

---
This meeting was scheduled via Multi-Agent Scheduler
"""
        
        return {
            "subject": subject,
            "body": body.format(organizer=organizer)
        }
    
    @staticmethod
    def meeting_reminder(data: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate a meeting reminder email
        
        Args:
            data: Dict with keys: recipient_name, date, start_time, end_time, 
                  meeting_topic, meeting_link, organizer_name
        
        Returns:
            Dict with 'subject' and 'body' keys
        """
        recipient_name = data.get("recipient_name", "there")
        date = data.get("date", "")
        start_time = data.get("start_time", "")
        end_time = data.get("end_time", "")
        topic = data.get("meeting_topic", "Meeting")
        meeting_link = data.get("meeting_link", "")
        organizer = data.get("organizer_name", "The Team")
        
        formatted_date = EmailTemplates.format_date(date)
        formatted_start = EmailTemplates.format_time(start_time)
        formatted_end = EmailTemplates.format_time(end_time)
        
        subject = f"⏰ Reminder: {topic} - {formatted_date}"
        
        body = f"""Hi {recipient_name},

This is a friendly reminder about your upcoming meeting.

⏰ MEETING REMINDER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Date: {formatted_date}
• Time: {formatted_start} - {formatted_end}
• Topic: {topic}
"""
        
        if meeting_link:
            body += f"• Meeting Link: {meeting_link}\n"
        
        body += """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Please make sure you're prepared for the meeting.

See you soon!

Best regards,
{organizer}

---
This meeting was scheduled via Multi-Agent Scheduler
"""
        
        return {
            "subject": subject,
            "body": body.format(organizer=organizer)
        }
    
    @staticmethod
    def meeting_cancellation(data: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate a meeting cancellation email
        
        Args:
            data: Dict with keys: recipient_name, date, start_time, meeting_topic,
                  reason, organizer_name
        
        Returns:
            Dict with 'subject' and 'body' keys
        """
        recipient_name = data.get("recipient_name", "there")
        date = data.get("date", "")
        start_time = data.get("start_time", "")
        topic = data.get("meeting_topic", "Meeting")
        reason = data.get("reason", "unforeseen circumstances")
        organizer = data.get("organizer_name", "The Team")
        
        formatted_date = EmailTemplates.format_date(date)
        formatted_start = EmailTemplates.format_time(start_time)
        
        subject = f"❌ Meeting Cancelled: {topic}"
        
        body = f"""Hi {recipient_name},

I regret to inform you that the meeting scheduled for {formatted_date} at {formatted_start} has been cancelled.

❌ CANCELLED MEETING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Date: {formatted_date}
• Time: {formatted_start}
• Topic: {topic}
• Reason: {reason}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I apologize for any inconvenience this may cause. I will reach out to you shortly to reschedule.

Best regards,
{organizer}

---
This meeting was scheduled via Multi-Agent Scheduler
"""
        
        return {
            "subject": subject,
            "body": body
        }
    
    @staticmethod
    def meeting_reschedule(data: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate a meeting reschedule email
        
        Args:
            data: Dict with keys: recipient_name, old_date, old_start_time,
                  new_date, new_start_time, new_end_time, meeting_topic,
                  reason, organizer_name
        
        Returns:
            Dict with 'subject' and 'body' keys
        """
        recipient_name = data.get("recipient_name", "there")
        old_date = data.get("old_date", "")
        old_start = data.get("old_start_time", "")
        new_date = data.get("new_date", "")
        new_start = data.get("new_start_time", "")
        new_end = data.get("new_end_time", "")
        topic = data.get("meeting_topic", "Meeting")
        reason = data.get("reason", "scheduling conflict")
        organizer = data.get("organizer_name", "The Team")
        
        old_formatted_date = EmailTemplates.format_date(old_date)
        old_formatted_time = EmailTemplates.format_time(old_start)
        new_formatted_date = EmailTemplates.format_date(new_date)
        new_formatted_start = EmailTemplates.format_time(new_start)
        new_formatted_end = EmailTemplates.format_time(new_end)
        
        subject = f"🔄 Meeting Rescheduled: {topic}"
        
        body = f"""Hi {recipient_name},

Due to {reason}, I need to reschedule our meeting.

🔄 RESCHEDULED MEETING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ Previous Schedule:
  • Date: {old_formatted_date}
  • Time: {old_formatted_time}

✓ New Schedule:
  • Date: {new_formatted_date}
  • Time: {new_formatted_start} - {new_formatted_end}
  
• Topic: {topic}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Please confirm if this new time works for you. I apologize for any inconvenience.

A new calendar invitation will be sent shortly.

Best regards,
{organizer}

---
This meeting was scheduled via Multi-Agent Scheduler
"""
        
        return {
            "subject": subject,
            "body": body
        }
    
    @staticmethod
    def availability_check(data: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate an email to check someone's availability
        
        Args:
            data: Dict with keys: recipient_name, date, start_time, end_time,
                  meeting_topic, organizer_name
        
        Returns:
            Dict with 'subject' and 'body' keys
        """
        recipient_name = data.get("recipient_name", "there")
        date = data.get("date", "")
        start_time = data.get("start_time", "")
        end_time = data.get("end_time", "")
        topic = data.get("meeting_topic", "a meeting")
        organizer = data.get("organizer_name", "The Team")
        
        formatted_date = EmailTemplates.format_date(date)
        formatted_start = EmailTemplates.format_time(start_time)
        formatted_end = EmailTemplates.format_time(end_time)
        
        subject = f"Checking Your Availability: {topic}"
        
        body = f"""Hi {recipient_name},

I hope you're doing well.

I'd like to schedule {topic} and wanted to check your availability.

📋 PROPOSED TIME:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Date: {formatted_date}
• Time: {formatted_start} - {formatted_end}
• Topic: {topic}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Please let me know if this time works for you or suggest an alternative.

Looking forward to hearing from you.

Best regards,
{organizer}

---
This meeting was scheduled via Multi-Agent Scheduler
"""
        
        return {
            "subject": subject,
            "body": body
        }
    
    @staticmethod
    def custom_email(data: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate a custom email with provided subject and message
        
        Args:
            data: Dict with keys: recipient_name, subject, message, organizer_name
        
        Returns:
            Dict with 'subject' and 'body' keys
        """
        recipient_name = data.get("recipient_name", "there")
        subject = data.get("subject", "Message from Multi-Agent Scheduler")
        message = data.get("message", "")
        organizer = data.get("organizer_name", "The Team")
        
        body = f"""Hi {recipient_name},

{message}

Best regards,
{organizer}

---
This message was sent via Multi-Agent Scheduler
"""
        
        return {
            "subject": subject,
            "body": body
        }


def get_template(template_type: str, data: Dict[str, Any]) -> Dict[str, str]:
    """
    Get email template by type
    
    Args:
        template_type: Type of template (invitation, confirmation, reminder, 
                      cancellation, reschedule, availability, custom)
        data: Data to populate the template
    
    Returns:
        Dict with 'subject' and 'body' keys
    """
    templates = {
        "invitation": EmailTemplates.meeting_invitation,
        "confirmation": EmailTemplates.meeting_confirmation,
        "reminder": EmailTemplates.meeting_reminder,
        "cancellation": EmailTemplates.meeting_cancellation,
        "reschedule": EmailTemplates.meeting_reschedule,
        "availability": EmailTemplates.availability_check,
        "custom": EmailTemplates.custom_email,
    }
    
    template_func = templates.get(template_type.lower())
    if not template_func:
        raise ValueError(f"Unknown template type: {template_type}")
    
    return template_func(data)
