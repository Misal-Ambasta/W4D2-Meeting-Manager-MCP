# Smart Meeting Assistant with AI Scheduling

## Usage Guide

This project uses the MCP Inspector for development and debugging. You can run the CLI in two ways:

**Recommended (with MCP Inspector):**

```bash
mcp dev main.py
```

This command launches the MCP Inspector, which provides a web-based interface for inspecting, testing, and debugging your MCP tools in real time. It is highly recommended for development and interactive testing.

**Direct CLI (without Inspector):**

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

### What is MCP Inspector?
MCP Inspector is a development tool that allows you to visually inspect and test your MCP tools (Python functions decorated with @mcp.tool). It provides a local web UI for easier debugging, input/output inspection, and rapid iteration. Use `mcp dev main.py` to launch your tools in Inspector mode.

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