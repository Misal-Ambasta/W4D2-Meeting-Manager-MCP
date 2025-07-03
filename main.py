from mcp.server.fastmcp import FastMCP
import mcp_tools

mcp = FastMCP(db_path="db.json")

@mcp.tool()
def create_meeting(title: str, participants: list, duration: int, preferences: dict):
    """Schedule a new meeting and add it to the database."""
    return mcp_tools.create_meeting(title, participants, duration, preferences)

@mcp.tool()
def find_optimal_slots(participants: list, duration: int, date_range: tuple):
    """Recommend optimal time slots for a meeting based on participant availability."""
    return mcp_tools.find_optimal_slots(participants, duration, date_range)

@mcp.tool()
def detect_scheduling_conflicts(user_id: str, time_range: tuple):
    """Detect scheduling conflicts for a user in a given time range."""
    return mcp_tools.detect_scheduling_conflicts(user_id, time_range)

@mcp.tool()
def analyze_meeting_patterns(user_id: str, period: tuple):
    """Analyze meeting patterns for a user in a given period."""
    return mcp_tools.analyze_meeting_patterns(user_id, period)

@mcp.tool()
def generate_agenda_suggestions(meeting_topic: str, participants: list):
    """Generate agenda suggestions based on topic and participants."""
    return mcp_tools.generate_agenda_suggestions(meeting_topic, participants)

@mcp.tool()
def calculate_workload_balance(team_members: list):
    """Calculate the number of meetings for each team member."""
    return mcp_tools.calculate_workload_balance(team_members)

@mcp.tool()
def score_meeting_effectiveness(meeting_id: str):
    """Assign an effectiveness score to a meeting."""
    return mcp_tools.score_meeting_effectiveness(meeting_id)

@mcp.tool()
def optimize_meeting_schedule(user_id: str):
    """Suggest an optimized meeting schedule for a user."""
    return mcp_tools.optimize_meeting_schedule(user_id)

if __name__ == "__main__":
    # Optionally run CLI or other logic here
    pass
