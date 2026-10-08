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

Run: python main.py

```text
PAWPAL+ | TODAY'S SCHEDULE
---------------------------------------------
09:00 | Luna: Breakfast (10 min) [priority: 3]
08:30 | Milo: Medication (15 min) [priority: 3]
08:00 | Luna: Morning walk (30 min) [priority: 3]
10:00 | Milo: Playtime (20 min) [priority: 1]
---------------------------------------------
Remaining time: 25 minutes
Deferred tasks: 0
Time conflicts: 0
```

## 🧪 Testing PawPal+

Run: python -m pytest -v

```text
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0 -- /Users/alejamora/Desktop/ai110-module2show-pawpal-starter/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/alejamora/Desktop/ai110-module2show-pawpal-starter
collecting ... collected 6 items

tests/test_pawpal.py::test_task_completion PASSED                        [ 16%]
tests/test_pawpal.py::test_task_addition PASSED                          [ 33%]
tests/test_pawpal.py::test_multi_pet_schedule PASSED                     [ 50%]
tests/test_pawpal.py::test_priority_sorting PASSED                       [ 66%]
tests/test_pawpal.py::test_time_constraint PASSED                        [ 83%]
tests/test_pawpal.py::test_completed_tasks_excluded PASSED               [100%]

============================== 6 passed in 0.05s ===============================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
