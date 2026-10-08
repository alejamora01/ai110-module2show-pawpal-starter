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

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
