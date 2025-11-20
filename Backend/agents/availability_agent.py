# agents/availability_agent.py

from availability import check_availability

class AvailabilityAgent:
    """
    Agent wrapper for checking Google Calendar availability.
    """

    def run(self, email: str, date: str, start_time: str, end_time: str):
        return check_availability(email, date, start_time, end_time)
