# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Implementation Summary

PawPal+ uses four Python classes:

- Task: stores activities and completion status.
- Pet: manages individual pet tasks.
- Owner: combines tasks from multiple pets.
- Scheduler: prioritizes tasks using available time.

Scheduler retrieves tasks through Owner.get_all_tasks().

## 🖥️ Sample Output

Generated with `python main.py`:

```text
PAWPAL+ | TODAY'S SCHEDULE
---------------------------------------------
08:00 | Milo: Breakfast (15 min)
08:10 | Ares: Morning walk (30 min)
12:00 | Milo: Playtime (20 min)
16:00 | Ares: Afternoon walk (30 min)
---------------------------------------------
Remaining minutes: 25

FILTER: ARES
Ares - Afternoon walk
Ares - Morning walk

CONFLICT DETECTION
WARNING: Breakfast overlaps with Morning walk

RECURRING TASK TEST
Completed: Breakfast
Next occurrence: 2026-10-08
Expected: 739897
Recurrence verified: True
```

## 🧪 Testing PawPal+

Run the automated tests with:

```bash
python -m pytest
```

### What I Tested

- Task completion and task addition
- Scheduling tasks from multiple pets
- Priority and chronological sorting
- Filtering by pet and completion status
- Daily and weekly recurring tasks
- Overlapping and adjacent time slots
- Empty task lists and future tasks
- Time constraints and duplicate prevention

### Actual Test Results

```text
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/alejamora/Desktop/ai110-module2show-pawpal-starter
collected 17 items

tests/test_edge_cases.py ......                                          [ 35%]
tests/test_pawpal.py ......                                              [ 70%]
tests/test_scheduling.py .....                                           [100%]

============================== 17 passed in 0.10s ==============================
```

### Confidence Level

**4/5 stars**

I feel confident about the core scheduling behavior because the automated tests cover normal scenarios and important edge cases. However, the scheduler does not automatically resolve time conflicts, and I would like to add more input validation.

## 📐 Smarter Scheduling

PawPal+ includes several scheduling algorithms.

| Feature | Method | Description |
|---|---|---|
| Sorting | `Scheduler.sort_by_time()` | Orders tasks chronologically using HH:MM. |
| Filtering | `Scheduler.filter_tasks()` | Filters tasks by pet name or completion status. |
| Conflict Detection | `Scheduler.detect_conflicts()` | Detects overlapping task durations, including across different pets. |
| Recurring Tasks | `Pet.complete_task()` and `Task.mark_complete()` | Creates the next daily or weekly task after completion. |
| Priority Scheduling | `Scheduler.generate_plan()` | Selects tasks based on priority and available minutes. |

### Algorithm Limitations

The scheduler prioritizes tasks based on importance and duration.
It detects overlapping time slots but does not automatically move
tasks to resolve conflicts.

Daily and weekly recurring tasks generate their next occurrence
when the current task is completed.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
