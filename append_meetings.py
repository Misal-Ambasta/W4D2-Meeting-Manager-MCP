"""
Script to append realistic meetings to db.json for MCP project.
Usage: python append_meetings.py
"""
import json
from datetime import datetime, timedelta
import random

# Load the existing db.json file
with open('db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

users = db['users']
meetings = db['meetings']

# Helper to pick random users
user_ids = [u['id'] for u in users]
timezones = [u['timezone'] for u in users]
meeting_types = ['recurring', 'one-time', 'workshop', 'review', 'strategy', 'planning', 'sync', 'customer', 'audit', 'brainstorming', 'deepdive', 'techtalk', 'allhands', 'demo', 'onboarding', 'briefing', 'update']
locations = [
    'Virtual - Zoom', 'Virtual - Teams', 'London HQ', 'Madrid Office', 'Chicago Office',
    'NYC HQ', 'Seoul HQ', 'Sydney Office', 'Bangalore Office', 'Design Studio',
    'Innovation Lab', 'Executive Conference Room', 'Customer Success Room', 'Main Auditorium', 'Sales Conference Room'
]

# Determine the next meeting id
start_idx = len(meetings) + 1
num_to_add = 60 - len(meetings)

agenda_samples = [
    ['Project updates', 'Blockers discussion', 'Next week planning'],
    ['Q3 roadmap review', 'Feature prioritization', 'Resource allocation'],
    ['Presentation review', 'Demo rehearsal', 'Q&A preparation'],
    ['Component library review', 'Accessibility updates', 'Documentation'],
    ['Team updates', 'Technical presentations', 'Q&A session'],
    ['Career development', 'Project feedback', 'Personal check-in'],
    ['Sprint goals', 'Story estimation', 'Capacity planning'],
    ['Campaign performance', 'Budget allocation', 'Next quarter planning'],
    ['Current architecture review', 'Scalability challenges', 'Migration plan'],
    ['Feedback analysis', 'Priority issues', 'Action items'],
    ['Research findings', 'User insights', 'Design recommendations'],
    ['Budget review', 'Resource allocation', 'Cost optimization'],
    ['API specification review', 'Security considerations', 'Documentation'],
    ['Pipeline review', 'Sales targets', 'Market analysis'],
    ['Project updates', 'Career goals', 'Team feedback'],
    ['Introductions', 'Project overview', 'Q&A'],
    ['Status update', 'Open issues', 'Next steps'],
    ['Design walkthrough', 'Feedback', 'Action items'],
    ['Task assignments', 'Risks', 'Sprint goals'],
    ['Policy changes', 'Compliance', 'Q&A'],
    ['Financials', 'KPIs', 'Next quarter planning'],
    ['Deployments', 'Monitoring', 'Incident response'],
    ['Customer insights', 'Feature requests', 'Support issues'],
    ['Project walkthrough', 'Model results', 'Next steps'],
    ['Audit checklist', 'Roles & responsibilities', 'Timeline'],
    ['Company vision', 'Leadership challenges', 'Open forum'],
    ['Test results', 'Bug triage', 'Release plan'],
    ['Content calendar', 'Resource allocation', 'Deadlines'],
    ['Migration status', 'Issues', 'Next steps'],
    ['Pipeline status', 'Forecasts', 'Challenges'],
    ['Project updates', 'Risks', 'Milestones'],
    ['Compliance overview', 'Action items', 'Q&A'],
    ['Closing checklist', 'Issues', 'Next month plan'],
    ['Architecture overview', 'Best practices', 'Q&A'],
    ['Company updates', 'Q&A', 'Recognition'],
    ['Research findings', 'Implications', 'Next steps'],
    ['Feature walkthrough', 'Feedback', 'Release plan'],
    ['Company intro', 'Policies', 'Q&A'],
    ['Privacy laws', 'Best practices', 'Q&A'],
    ['Challenge overview', 'Team formation', 'Timeline'],
    ['Strategic goals', 'Resource planning', 'Risks']
]

def random_datetime(start_date, days_range):
    base = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%SZ')
    delta = timedelta(days=random.randint(0, days_range), hours=random.randint(0, 23), minutes=random.choice([0, 15, 30, 45]))
    return base + delta

for i in range(num_to_add):
    mid = f"meeting_{start_idx + i:03d}"
    organizer = random.choice(user_ids)
    participants = random.sample(user_ids, k=random.randint(2, min(5, len(user_ids))))
    tz = random.choice(timezones)
    mtype = random.choice(meeting_types)
    location = random.choice(locations)
    agenda = random.choice(agenda_samples)
    start = random_datetime('2024-08-20T09:00:00Z', 30)
    duration = timedelta(minutes=random.choice([30, 45, 60, 90]))
    end = start + duration
    meeting = {
        "id": mid,
        "title": f"Auto-Generated Meeting {start_idx + i}",
        "description": f"This is an auto-generated meeting for testing purposes.",
        "organizer": organizer,
        "participants": participants,
        "start_time": start.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "end_time": end.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "timezone": tz,
        "meeting_type": mtype,
        "location": location,
        "status": "confirmed",
        "agenda": agenda,
        "effectiveness_score": round(random.uniform(7.0, 9.5), 1),
        "created_at": (start - timedelta(days=random.randint(1, 7))).strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    meetings.append(meeting)

# Write back the updated db.json
with open('db.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Appended {num_to_add} meetings. Total meetings: {len(meetings)}")
