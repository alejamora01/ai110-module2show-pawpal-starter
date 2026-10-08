from datetime import date, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def test_pet_with_no_tasks():
    owner = Owner("Alejandra", 60)
    owner.add_pet(Pet("Ares", "Dog", 3))

    result = Scheduler().generate_plan(owner)

    assert result["scheduled"] == []
    assert result["remaining_minutes"] == 60


def test_identical_times_across_pets():
    ares = Pet("Ares", "Dog", 3)
    milo = Pet("Milo", "Cat", 2)

    tasks = [
        (ares, Task("Walk", 30, 3, start_time="08:00")),
        (milo, Task("Feed", 15, 3, start_time="08:00"))
    ]

    assert len(Scheduler().detect_conflicts(tasks)) == 1


def test_adjacent_times_not_conflicting():
    pet = Pet("Ares", "Dog", 3)

    tasks = [
        (pet, Task("Walk", 30, 3, start_time="08:00")),
        (pet, Task("Feed", 15, 3, start_time="08:30"))
    ]

    assert Scheduler().detect_conflicts(tasks) == []


def test_future_task_not_scheduled_today():
    owner = Owner("Alejandra", 60)
    pet = Pet("Milo", "Cat", 2)

    pet.add_task(Task(
        "Vet Visit", 30, 3,
        due_date=date.today() + timedelta(days=1)
    ))

    owner.add_pet(pet)

    result = Scheduler().generate_plan(owner)

    assert len(result["scheduled"]) == 0


def test_flexible_tasks_sorted_last():
    pet = Pet("Ares", "Dog", 3)

    tasks = [
        (pet, Task("Play", 20, 1)),
        (pet, Task("Walk", 30, 3, start_time="09:00")),
        (pet, Task("Feed", 10, 3, start_time="08:00"))
    ]

    result = Scheduler().sort_by_time(tasks)

    assert [task.name for _, task in result] == [
        "Feed", "Walk", "Play"
    ]


def test_repeating_task_not_duplicated():
    pet = Pet("Milo", "Cat", 2)
    task = Task("Medication", 10, 3, recurrence="daily")

    pet.add_task(task)

    first = pet.complete_task(task)
    second = pet.complete_task(task)

    assert first is not None
    assert second is None
    assert len(pet.tasks) == 2
