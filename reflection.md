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

I used AI throughout the project to brainstorm my UML
design, implement Python classes, plan algorithms, and
create automated tests. VS Code AI was especially useful
for reviewing my class relationships and comparing
different approaches to conflict detection.

I worked with separate AI discussions for design,
implementation, algorithms, and testing. This helped
me keep each phase focused.

**b. Judgment and verification**

One suggestion I decided not to implement was adding
a separate ScheduleEntry class. I wanted to keep
my initial architecture simple with four main classes.

AI also compared my nested-loop conflict detection
with an event-sweep algorithm. I kept the simpler
version because readability was more important
for a small household scheduling application.

I also had to correct a Python 3.9 compatibility
problem involving type annotations.

Instead of assuming AI-generated code worked,
I ran the CLI demo and verified the behavior
through automated tests.

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, task addition, multi-pet scheduling, priority sorting, time constraints, and completed task filtering.

**b. Confidence**

I would rate my current system 4 out of 5 stars.

My automated tests cover basic operations, multiple pets,
sorting, filtering, recurrence, and scheduling edge cases.

I verified the implementation using pytest instead of
assuming the generated code was correct.

I still want to improve input validation and automatic
conflict resolution. These are important limitations
that I would address in another iteration.

---

## 5. Reflection

**a. What went well**

I am most satisfied with connecting my object-oriented
Python backend to the Streamlit interface. I was able
to create a system where multiple pets share one
owner's available time.

I also improved my testing process by adding
edge cases instead of checking only basic behavior.

**b. What you would improve**

If I had another iteration, I would implement
automatic conflict resolution and stronger input
validation. I would also consider permanent data
storage so information remains available after
the Streamlit session ends.

**c. Key takeaway**

My biggest takeaway is that AI is helpful for
brainstorming, coding, and debugging, but I still
need to make the final engineering decisions.

Being the lead architect means understanding
the design, evaluating tradeoffs, running tests,
and verifying that the implementation meets
the actual project requirements.
