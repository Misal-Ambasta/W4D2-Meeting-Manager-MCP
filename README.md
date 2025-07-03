# Smart Meeting Assistant with AI Scheduling

## Usage Guide

Run the CLI:

```bash
python main.py
```

You will see a menu to:
- Create meetings
- Find optimal slots
- Detect conflicts
- Analyze patterns
- Generate agenda
- Calculate workload
- Score effectiveness
- Optimize schedule
- List users/meetings

Follow prompts to test each MCP tool interactively.

## Data Schema

### User
```
{
  "id": "user_001",
  "name": "...",
  "email": "...",
  "timezone": "...",
  "working_hours": {"start": "HH:MM", "end": "HH:MM"},
  "preferences": { ... }
}
```

### Meeting
```
{
  "id": "meeting_001",
  "title": "...",
  "description": "...",
  "organizer": "user_001",
  "participants": ["user_001", ...],
  "start_time": "YYYY-MM-DDTHH:MM:SSZ",
  "end_time": "YYYY-MM-DDTHH:MM:SSZ",
  "timezone": "...",
  "meeting_type": "...",
  "location": "...",
  "status": "confirmed",
  "agenda": [ ... ],
  "effectiveness_score": 8.5,
  "created_at": "YYYY-MM-DDTHH:MM:SSZ"
}
```

## Assumptions
- All data is stored in `db.json` (no external DB required)
- Time zones are respected for users and meetings
- MCP tools are Python functions, not web APIs
- CLI is for demo and testing purposes