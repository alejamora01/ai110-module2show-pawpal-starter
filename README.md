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

## Features

- Manage multiple pets through a single owner profile.
- Create care tasks with duration, priority, date, and time.
- Sort tasks chronologically.
- Filter tasks by pet and completion status.
- Generate daily schedules based on available minutes.
- Create the next daily or weekly occurrence after completion.
- Detect overlapping timed tasks and display warnings.
- Keep owner and pet objects in Streamlit session state.

## System Architecture

The app separates the Streamlit interface (`app.py`)
from the OOP backend (`pawpal_system.py`).

The final Mermaid class diagram is available at
`diagrams/uml_final.mmd`.

## 🖥️ Sample Output

Output from `python main.py`:

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

Run `python -m pytest`.

The tests cover core scheduling, multiple pets, sorting, filtering, recurrence, conflicts, edge cases, and next available slot detection.

**Confidence: 4/5 stars.**

```text
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/alejamora/Desktop/ai110-module2show-pawpal-starter
collected 22 items

tests/test_available_slot.py .....                                       [ 22%]
tests/test_edge_cases.py ......                                          [ 50%]
tests/test_pawpal.py ......                                              [ 77%]
tests/test_scheduling.py .....                                           [100%]

============================== 22 passed in 0.20s ==============================
```

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

1. Start the app using `python -m streamlit run app.py`.
2. Enter an owner name and available minutes.
3. Add two pets, such as Ares and Milo.
4. Add care tasks with durations, priorities, dates, and times.
5. Use the Task Manager to filter by pet or completion status.
6. Select Generate Schedule to display today's tasks.
7. Review remaining time, deferred tasks, and conflict warnings.
8. Mark a recurring task complete and check its next due date.

### Scheduling behavior

Tasks are selected by priority and available minutes, and
displayed in chronological order where times are provided.

Tasks with overlapping time intervals generate warnings.
The app does not automatically move overlapping tasks.

Daily and weekly recurring tasks create their next
occurrence when completed.

### CLI Demonstration

The verified CLI output is included in the Sample Output
section above. The same backend powers Streamlit.

## Advanced Algorithmic Capability

### Next Available Slot

PawPal+ includes `Scheduler.find_next_available_slot()`.

This method finds the earliest available time for a new
task within a specified daily time window.

It considers scheduled tasks across multiple pets,
their durations, and overlapping intervals.

For example, if tasks occupy 08:00-08:30 and
08:30-09:00, a new 20-minute task can start at 09:00.

The method returns `None` when no suitable slot exists.

The implementation uses sorted occupied intervals
rather than checking every minute individually.

