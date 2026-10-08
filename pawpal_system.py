from dataclasses import dataclass, field, replace
from datetime import date, datetime, timedelta
from typing import Optional


@dataclass
class Task:
    """Represent a pet care activity."""
    name: str
    duration: int
    priority: int
    category: str = "general"
    start_time: Optional[str] = None
    recurrence: str = "none"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Complete a task and return its next occurrence."""
        self.completed = True

        days = {"daily": 1, "weekly": 7}
        frequency = self.recurrence.lower()

        if frequency not in days:
            return None

        return replace(
            self,
            due_date=self.due_date + timedelta(
                days=days[frequency]
            ),
            completed=False
        )


@dataclass
class Pet:
    """Store pet details and care tasks."""
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def complete_task(self, task: Task):
        """Complete a task and store its next occurrence."""
        if task not in self.tasks:
            raise ValueError("Task does not belong to this pet.")

        if task.completed:
            return None

        next_task = task.mark_complete()

        if next_task is not None:
            self.add_task(next_task)

        return next_task


@dataclass
class Owner:
    """Manage pets and their combined care tasks."""
    name: str
    available_minutes: int
    preferences: list = field(default_factory=list)
    pets: list = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Register a pet with this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return tasks from every registered pet."""
        return [
            (pet, task)
            for pet in self.pets
            for task in pet.tasks
        ]


class Scheduler:
    """Organize care tasks across multiple pets."""

    def sort_tasks(self, tasks):
        """Sort by priority and then duration."""
        return sorted(
            tasks,
            key=lambda item: (
                -item[1].priority,
                item[1].duration
            )
        )

    def sort_by_time(self, tasks):
        """Sort tasks by HH:MM, placing flexible tasks last."""
        return sorted(
            tasks,
            key=lambda item: (
                item[1].start_time is None,
                item[1].start_time or "99:99"
            )
        )

    def filter_tasks(
        self, tasks, pet_name=None, completed=None
    ):
        """Filter tasks by pet and completion status."""
        return [
            (pet, task)
            for pet, task in tasks
            if (
                pet_name is None
                or pet.name.lower() == pet_name.lower()
            )
            and (
                completed is None
                or task.completed == completed
            )
        ]

    def generate_recurring_tasks(self, tasks):
        """Select active tasks due today or earlier."""
        today = date.today()

        return [
            (pet, task)
            for pet, task in tasks
            if not task.completed
            and task.due_date <= today
        ]

    def detect_conflicts(self, tasks):
        """Find overlapping tasks on the same date."""
        timed = []

        for pet, task in tasks:
            if task.completed or not task.start_time:
                continue

            start = datetime.combine(
                task.due_date,
                datetime.strptime(
                    task.start_time, "%H:%M"
                ).time()
            )
            end = start + timedelta(
                minutes=task.duration
            )

            timed.append((pet, task, start, end))

        conflicts = []

        for i in range(len(timed)):
            for j in range(i + 1, len(timed)):
                first = timed[i]
                second = timed[j]

                if (
                    first[2] < second[3]
                    and second[2] < first[3]
                ):
                    conflicts.append(
                        (first[1], second[1])
                    )

        return conflicts

    def generate_plan(self, owner: Owner):
        """Build a priority-based plan for all pets."""
        tasks = owner.get_all_tasks()
        tasks = self.generate_recurring_tasks(tasks)
        tasks = self.sort_tasks(tasks)

        remaining = owner.available_minutes
        scheduled = []
        deferred = []

        for pet, task in tasks:
            if task.duration <= remaining:
                scheduled.append((pet, task))
                remaining -= task.duration
            else:
                deferred.append((pet, task))

        return {
            "scheduled": scheduled,
            "deferred": deferred,
            "remaining_minutes": remaining,
        }
