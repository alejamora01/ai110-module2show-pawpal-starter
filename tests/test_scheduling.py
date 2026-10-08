from datetime import date, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def test_sort_by_time():
    pet = Pet("Ares", "Dog", 3)
    tasks = [
        (pet, Task("Late", 10, 1, start_time="16:00")),
        (pet, Task("Early", 10, 1, start_time="08:00"))
    ]
    result = Scheduler().sort_by_time(tasks)
    assert result[0][1].name == "Early"


def test_filter_by_pet_and_status():
    ares = Pet("Ares", "Dog", 3)
    milo = Pet("Milo", "Cat", 2)
    tasks = [
        (ares, Task("Walk", 20, 2)),
        (milo, Task("Feed", 10, 3)),
        (ares, Task("Bath", 20, 1, completed=True))
    ]
    result = Scheduler().filter_tasks(
        tasks, pet_name="Ares", completed=False
    )
    assert len(result) == 1
    assert result[0][1].name == "Walk"


def test_daily_recurrence():
    pet = Pet("Milo", "Cat", 2)
    task = Task("Feed", 10, 3, recurrence="daily")
    pet.add_task(task)
    next_task = pet.complete_task(task)

    assert task.completed is True
    assert next_task.due_date == date.today() + timedelta(days=1)
    assert len(pet.tasks) == 2


def test_weekly_recurrence():
    pet = Pet("Ares", "Dog", 3)
    task = Task("Grooming", 30, 2, recurrence="weekly")
    pet.add_task(task)
    next_task = pet.complete_task(task)

    assert next_task.due_date == date.today() + timedelta(days=7)


def test_overlapping_tasks():
    pet = Pet("Ares", "Dog", 3)
    tasks = [
        (pet, Task("Walk", 30, 3, start_time="08:00")),
        (pet, Task("Feed", 10, 3, start_time="08:15"))
    ]
    assert len(Scheduler().detect_conflicts(tasks)) == 1
