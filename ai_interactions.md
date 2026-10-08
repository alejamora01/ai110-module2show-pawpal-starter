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
