from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration: int
    priority: int
    category: str = "general"
    start_time: str | None = None
    recurrence: str = "none"
    completed: bool = False

    def mark_complete(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass


@dataclass
class Owner:
    name: str
    available_minutes: int
    preferences: list[str] = field(default_factory=list)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        pass


class Scheduler:

    def sort_tasks(self, tasks: list[Task]):
        pass

    def detect_conflicts(self, tasks: list[Task]):
        pass

    def generate_plan(self, owner: Owner):
        pass

    def generate_recurring_tasks(self, tasks: list[Task]):
        pass
