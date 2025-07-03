from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
import random
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'db.json')

def load_db() -> dict:
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_db(db: dict) -> None:
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2)

def create_meeting(title: str, participants: List[str], duration: int, preferences: Dict[str, Any]) -> Dict[str, Any]:
    """
    Schedule a new meeting and add it to the database.

    Parameters:
        title (str): The meeting title. Example: "AI Sync"
        participants (list of str): List of user IDs. Example: ["user_001", "user_002"]
        duration (int): Duration in minutes. Example: 30
        preferences (dict): Organizer preferences. Example:
            {
                "organizer": "user_001",
                "preferred_start_time": "2024-08-01T10:00:00Z",
                "description": "Weekly AI sync-up"
            }

    Returns:
        dict: The created meeting object.

    Example call:
        create_meeting(
            title="AI Sync",
            participants=["user_001", "user_002"],
            duration=30,
            preferences={
                "organizer": "user_001",
                "preferred_start_time": "2024-08-01T10:00:00Z",
                "description": "Weekly AI sync-up"
            }
        )
    """
    print(preferences, participants, duration, title)
    start_time = preferences.get('preferred_start_time', '2024-08-01T10:00:00Z')
    end_time = (datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ') + timedelta(minutes=duration)).strftime('%Y-%m-%dT%H:%M:%SZ')
    db = load_db()
    if not participants:
        raise ValueError("At least one participant is required to create a meeting.")
    meeting = {
        "id": f"meeting_{len(db['meetings'])+1:03d}",
        "title": title,
        "description": preferences.get('description', ''),
        "organizer": preferences.get('organizer', participants[0]),
        "participants": participants,
        "start_time": start_time,
        "end_time": end_time,
        "timezone": preferences.get('timezone', 'UTC'),
        "meeting_type": preferences.get('meeting_type', 'one-time'),
        "location": preferences.get('location', 'Virtual'),
        "status": "confirmed",
        "agenda": preferences.get('agenda', []),
        "effectiveness_score": None,
        "created_at": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    db['meetings'].append(meeting)
    save_db(db)
    return meeting

def find_optimal_slots(participants: List[str], duration: int, date_range: Tuple[str, str]) -> List[str]:
    """
    Recommend optimal time slots for a meeting based on participant availability.

    Parameters:
        participants (list of str): List of user IDs. Example: ["user_001", "user_002"]
        duration (int): Desired meeting duration in minutes. Example: 30
        date_range (tuple of str): Date range as (start, end) in 'YYYY-MM-DD' format. Example: ("2024-08-01", "2024-08-05")

    Returns:
        list of str: List of recommended start times (ISO format).

    Example call:
        find_optimal_slots(["user_001", "user_002"], 30, ("2024-08-01", "2024-08-05"))
    """
    # Example dummy logic: return 3 slots at 10am on consecutive days in the range
    start = datetime.strptime(date_range[0], '%Y-%m-%d')
    slots = [(start + timedelta(days=i)).strftime('%Y-%m-%dT10:00:00Z') for i in range(3)]
    return slots

def detect_scheduling_conflicts(user_id: str, time_range: Tuple[str, str]) -> List[Dict[str, Any]]:
    """
    Detect scheduling conflicts for a user in a given time range.

    Parameters:
        user_id (str): The user ID. Example: "user_001"
        time_range (tuple of str): Time range as (start, end) in ISO format. Example: ("2024-08-01T09:00:00Z", "2024-08-01T11:00:00Z")

    Returns:
        list of dict: List of conflicting meetings.

    Example call:
        detect_scheduling_conflicts("user_001", ("2024-08-01T09:00:00Z", "2024-08-01T11:00:00Z"))
    """
    db = load_db()
    user_meetings = [m for m in db['meetings'] if user_id in m['participants']]
    conflicts = []
    range_start = datetime.strptime(time_range[0], '%Y-%m-%dT%H:%M:%SZ')
    range_end = datetime.strptime(time_range[1], '%Y-%m-%dT%H:%M:%SZ')
    for m in user_meetings:
        m_start = datetime.strptime(m['start_time'], '%Y-%m-%dT%H:%M:%SZ')
        m_end = datetime.strptime(m['end_time'], '%Y-%m-%dT%H:%M:%SZ')
        if m_start < range_end and m_end > range_start:
            conflicts.append(m)
    return conflicts

def analyze_meeting_patterns(user_id: str, period: Tuple[str, str]) -> Dict[str, Any]:
    """
    Analyze meeting patterns for a user in a given period.

    Parameters:
        user_id (str): The user ID. Example: "user_001"
        period (tuple of str): Period as (start, end) in 'YYYY-MM-DD' format. Example: ("2024-08-01", "2024-08-31")

    Returns:
        dict: Meeting pattern statistics (total meetings, average duration).

    Example call:
        analyze_meeting_patterns("user_001", ("2024-08-01", "2024-08-31"))
    """
    db = load_db()
    meetings = [m for m in db['meetings'] if user_id in m['participants']]
    start = datetime.strptime(period[0], '%Y-%m-%d')
    end = datetime.strptime(period[1], '%Y-%m-%d')
    filtered = [m for m in meetings if start <= datetime.strptime(m['start_time'], '%Y-%m-%dT%H:%M:%SZ') <= end]
    total = len(filtered)
    durations = [
        (datetime.strptime(m['end_time'], '%Y-%m-%dT%H:%M:%SZ') - datetime.strptime(m['start_time'], '%Y-%m-%dT%H:%M:%SZ')).total_seconds()/60
        for m in filtered
    ]
    avg_duration = sum(durations)/total if total else 0
    return {"total_meetings": total, "average_duration": avg_duration}

def generate_agenda_suggestions(meeting_topic: str, participants: List[str]) -> List[str]:
    """
    Generate agenda suggestions based on topic and participants.

    Parameters:
        meeting_topic (str): The meeting topic. Required format: string. Example: "AI Project"
        participants (list of str): List of user IDs. Required format: list of strings. Example: ["user_001", "user_002"]

    Returns:
        list of str: Suggested agenda items.

    Example call:
        generate_agenda_suggestions("AI Project", ["user_001", "user_002"])
    """
    base_agenda = [f"Discuss {meeting_topic}", "Review action items", "Q&A"]
    return base_agenda

def calculate_workload_balance(team_members: List[str]) -> Dict[str, int]:
    """
    Calculate the number of meetings for each team member.

    Parameters:
        team_members (list of str): List of user IDs. Example: ["user_001", "user_002", "user_003"]

    Returns:
        dict: Mapping from user ID to meeting count.

    Example call:
        calculate_workload_balance(["user_001", "user_002", "user_003"])
    """
    db = load_db()
    meetings = db['meetings']
    return {member: sum(member in m['participants'] for m in meetings) for member in team_members}

def score_meeting_effectiveness(meeting_id: str) -> float:
    """
    Assign a random effectiveness score to a meeting (dummy logic).

    Parameters:
        meeting_id (str): The meeting ID. Example: "meeting_001"

    Returns:
        float: The effectiveness score assigned.

    Example call:
        score_meeting_effectiveness("meeting_001")
    """
    db = load_db()
    meeting = next((m for m in db['meetings'] if m['id'] == meeting_id), None)
    score = round(random.uniform(7.0, 10.0), 1)
    if meeting:
        meeting['effectiveness_score'] = score
        save_db(db)
    return score

def optimize_meeting_schedule(user_id: str) -> List[Dict[str, Any]]:
    """
    Suggest an optimized meeting schedule for a user.

    Parameters:
        user_id (str): The user ID. Example: "user_001"

    Returns:
        list of dict: List of meetings in optimized order.

    Example call:
        optimize_meeting_schedule("user_001")
    """
    db = load_db()
    meetings = [m for m in db['meetings'] if user_id in m['participants']]
    meetings.sort(key=lambda m: m['start_time'])
    return meetings
