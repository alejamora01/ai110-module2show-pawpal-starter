# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF7)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Prompt Comparison (SF11)

> Compare two different prompts (or two different models) on the same task.

| | Option A | Option B |
|-|----------|----------|
| **Model / tool used** | | |
| **Prompt** | | |
| **Response summary** | | |
| **What was useful** | | |
| **Problems noticed** | | |
| **Decision** | | |

**Which approach did you use in your final implementation and why?**

<!-- Your conclusion -->

## Phase 1: System Design

### AI design assistance

I used ChatGPT to brainstorm the initial class responsibilities,
create a Mermaid UML draft, and scaffold Python class stubs.

I chose to keep four classes: Owner, Pet, Task, and Scheduler.

The design separates pet information from scheduling logic.

### VS Code AI review prompt

Review my PawPal+ system design in pawpal_system.py and
diagrams/uml_draft.mmd. Check class responsibilities,
relationships, and potential scheduling bottlenecks.
Do not implement algorithms yet.

### Review outcome

To be completed after reviewing the AI assistant's feedback.

### Phase 1: AI Review Results

The VS Code AI assistant reviewed my Python skeleton and UML.

It identified several design risks:
- Available time could be counted separately for multiple pets.
- Task did not contain enough scheduling information.
- A boolean recurring field was too limited.
- Owner preferences were not connected to task categories.
- The scheduler did not explain deferred tasks.

I accepted the recommendations to schedule by owner, add start_time, use a recurrence field, and include task categories.

I decided not to introduce an additional ScheduleEntry class yet because the initial design should stay manageable.

Deferred tasks and scheduling explanations will be considered during implementation.

I will verify these decisions with tests in later phases.

## Phase 3: Streamlit Integration

I used AI to connect the Streamlit interface to my
Python object-oriented backend.

I used st.session_state to keep the Owner object
and its pets available across Streamlit reruns.

The Add Pet button calls Owner.add_pet().
The Add Task button calls Pet.add_task().
The Generate Schedule button calls Scheduler.generate_plan().

I verified the integration through browser interactions
and checked that the existing backend tests still pass.

## Phase 3: Streamlit Integration

I used AI to help connect the Streamlit UI to my Python classes.

I implemented st.session_state to preserve the Owner object across Streamlit reruns.

The Add Pet form calls Owner.add_pet(), and the Add Task form calls Pet.add_task().

I tested the app in the browser by adding two pets, Ares and Milo, and assigning tasks to both.

The Scheduler successfully generated a daily plan showing both pets, their tasks, and 80 remaining minutes.

I verified that the interface uses my backend classes instead of placeholder data.

## Phase 4: Algorithm Evaluation

I asked my AI coding assistant to review Scheduler.detect_conflicts()
and suggest a more efficient alternative.

The AI compared my nested-loop algorithm with an event-sweep
algorithm.

My implementation:
- Time complexity: O(n^2)
- Space complexity: O(n + k)
- Easy to read and debug

AI alternative:
- Time complexity: O(n log n + k)
- Space complexity: O(n + k)
- Better for larger schedules

I decided to keep the nested-loop implementation because PawPal+
is designed for a small number of household pet tasks.

Although the event-sweep algorithm is more efficient for large
inputs, the original version is easier to understand, maintain,
and verify.

I did not change the implementation after this review.

## Phase 5: Testing and Verification

I used AI to support testing and identify edge cases
that were missing from the original test suite.

I focused on empty schedules, identical start times
across pets, adjacent tasks, future due dates,
chronological sorting, and recurring task duplication.

I used pytest to verify the actual behavior of the
Python classes instead of relying only on the CLI demo.

I also considered the limitation that conflict detection
does not automatically resolve overlapping tasks.

## Phase 6: Final Architecture and UI

I used AI to review my final UML structure and
to help connect the scheduling algorithms to the UI.

I updated the UI to show sorted schedules,
task filters, recurrence options, and conflict warnings.

I kept the original four-class architecture.
I verified the backend using pytest and reviewed
the interface manually through Streamlit.

I documented limitations, including the lack
of automatic conflict resolution and persistent storage.
