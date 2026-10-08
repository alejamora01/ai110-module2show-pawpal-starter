# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

For my initial design, I wanted PawPal+ to be simple and organized so pet owners can manage their pets' routines.

The three main actions are:
1. Add a pet and save its basic information.
2. Create and manage care tasks like feeding, walking, and medication.
3. Generate a daily plan based on available time and task priorities.

I chose four main classes:

- **Owner:** Stores the owner's name, available time, preferences, and pets.
- **Pet:** Stores each pet's basic information and care tasks.
- **Task:** Represents a care activity with a duration, priority, and completion status.
- **Scheduler:** Organizes tasks based on priorities, available time, and scheduling constraints.

I separated these responsibilities to make the system easier to understand, test, and improve.

**b. Design changes**

After reviewing my initial design with AI, I noticed a few things that could make my scheduler more reliable.

First, I changed generate_plan to use the Owner instead of one Pet because the owner's available time should be shared across all pets.

I also added start_time to Task so the scheduler can eventually detect overlapping activities. I replaced the recurring boolean with a recurrence field to support different repeating schedules, and added a category to help connect tasks with owner preferences.

I decided to keep the original four classes because I wanted my design to stay simple and easy to maintain. I did not add a separate ScheduleEntry class yet because I want to implement and test the basic scheduling logic first.

These changes are still part of the design. I will verify their behavior during implementation and testing.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers task priority, duration, completion status, due dates, and the owner's available time.

I chose to prioritize higher-priority tasks first because activities like medication and feeding can be more important than optional activities.

I also implemented sorting by time, filtering by pet or status, recurring tasks, and conflict detection.

**b. Tradeoffs**

One tradeoff I made was choosing readability over performance
for conflict detection.

My current algorithm uses nested loops to compare task intervals.
It has O(n^2) time complexity.

AI suggested an event-sweep alternative with
O(n log n + k) complexity, where k is the number of conflicts.

I decided to keep my original algorithm because PawPal+
handles a relatively small number of tasks.

I also chose to detect scheduling conflicts without
automatically rescheduling activities. This keeps the
implementation simple while still warning pet owners
about overlapping tasks.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI to help implement the four Python classes, understand multi-pet scheduling, and create automated tests. AI also helped me solve a Python 3.9 compatibility error.

**b. Judgment and verification**

AI suggested adding a separate ScheduleEntry class, but I decided to keep the original four classes to avoid unnecessary complexity.

I verified my implementation using a CLI demo and automated tests. I also corrected the unsupported type annotation using Optional[str].

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, task addition, multi-pet scheduling, priority sorting, time constraints, and completed task filtering.

**b. Confidence**

All six tests passed, and my CLI demo successfully generated a schedule for two pets. I still want to improve recurring tasks and conflict handling in future phases.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
