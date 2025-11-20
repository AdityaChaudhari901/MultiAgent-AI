# agents/scheduler_agent.py
from typing import List, Dict
from scheduler import schedule_meeting

class SchedulerAgent:
    """
    Wrapper around schedule_meeting function.
    """

    def run(self, summary: str, description: str, date: str, start_time: str, end_time: str, attendees: List[str]) -> Dict:
        """
        Creates calendar event and returns creation result.
        """
        return schedule_meeting(summary=summary, description=description, date=date, start_time=start_time, end_time=end_time, attendees=attendees)
