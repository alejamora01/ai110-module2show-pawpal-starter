from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class Task:
    name: str
    duration: int
    priority: int
    category: str = "general"
    start_time: Optional[str] = None
    recurrence: str = "none"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a care task to this pet."""
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    available_minutes: int
    preferences: list[str] = field(default_factory=list)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Register a pet with this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks paired with their pets."""
        return [
            (pet, task)
            for pet in self.pets
            for task in pet.tasks
        ]


class Scheduler:
    def sort_tasks(self, tasks):
        """Sort tasks by priority, then duration."""
        return sorted(
            tasks,
            key=lambda item: (-item[1].priority, item[1].duration)
        )

    def detect_conflicts(self, tasks):
        """Find overlapping fixed-time tasks."""
        scheduled = []

        for pet, task in tasks:
            if task.start_time and not task.completed:
                start = datetime.strptime(task.start_time, "%H:%M")
                end = start + timedelta(minutes=task.duration)
                scheduled.append((pet, task, start, end))

        conflicts = []

        for i in range(len(scheduled)):
            for j in range(i + 1, len(scheduled)):
                first = scheduled[i]
                second = scheduled[j]

                if first[2] < second[3] and second[2] < first[3]:
                    conflicts.append((first[1], second[1]))

        return conflicts

    def generate_recurring_tasks(self, tasks):
        """Return active tasks, including recurring tasks."""
        return [
            item for item in tasks
            if not item[1].completed
        ]

    def generate_plan(self, owner: Owner):
        """Create a daily plan across all owner's pets."""
        tasks = owner.get_all_tasks()
        tasks = self.generate_recurring_tasks(tasks)
        tasks = self.sort_tasks(tasks)

        remaining = owner.available_minutes
        plan = []
        deferred = []

        for pet, task in tasks:
            if task.duration <= remaining:
                plan.append((pet, task))
                remaining -= task.duration
            else:
                deferred.append((pet, task))

        return {
            "scheduled": plan,
            "deferred": deferred,
            "remaining_minutes": remaining,
        }
