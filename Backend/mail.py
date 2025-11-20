from utils.google_client import get_gmail_service
from email.mime.text import MIMEText
import base64

def send_email(to, subject, message):
    service = get_gmail_service()

    mime_message = MIMEText(message)
    mime_message["to"] = to
    mime_message["subject"] = subject

    encoded_message = base64.urlsafe_b64encode(
        mime_message.as_bytes()).decode()

    body = {
        "raw": encoded_message
    }

    sent = service.users().messages().send(userId="me", body=body).execute()
    return {"status": "Email Sent", "id": sent["id"]}
