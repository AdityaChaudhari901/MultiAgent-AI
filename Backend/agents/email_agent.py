# agents/email_agent.py
from typing import Dict, Any, Optional
from mail import send_email
from templates.email_templates import get_template

class EmailAgent:
    """
    Wrapper around send_email function with template support.
    """

    def run(self, to: str, subject: str, message: str, 
            template_type: Optional[str] = None,
            template_data: Optional[Dict[str, Any]] = None) -> Dict:
        """
        Sends an email and returns the result.
        
        Args:
            to: Recipient email address
            subject: Email subject (used if no template)
            message: Email message (used if no template)
            template_type: Optional template type (invitation, confirmation, etc.)
            template_data: Optional data for template rendering
        
        Returns:
            Dict with status and message
        """
        # Use template if provided
        if template_type and template_data:
            try:
                template_content = get_template(template_type, template_data)
                subject = template_content["subject"]
                message = template_content["body"]
            except Exception as e:
                print(f"Template error: {e}, using provided subject/message")
        
        return send_email(to=to, subject=subject, message=message)
