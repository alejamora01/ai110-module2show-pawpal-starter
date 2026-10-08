import pytest
from pawpal_system import Owner, Pet, Task, Scheduler


def make_owner():
    owner = Owner("Alejandra", 180)
    ares = Pet("Ares", "Dog", 3)
    milo = Pet("Milo", "Cat", 2)

    ares.add_task(Task(
        "Walk", 30, 3, start_time="08:00"
    ))
    milo.add_task(Task(
        "Feeding", 30, 3, start_time="08:30"
    ))

    owner.add_pet(ares)
    owner.add_pet(milo)
    return owner


def test_next_available_slot_multiple_pets():
    result = Scheduler().find_next_available_slot(
        make_owner(), 20, "08:00", "11:00"
    )
    assert result == "09:00"


def test_empty_schedule():
    owner = Owner("Alejandra", 120)
    assert Scheduler().find_next_available_slot(
        owner, 30, "08:00", "10:00"
    ) == "08:00"


def test_full_schedule():
    owner = make_owner()
    assert Scheduler().find_next_available_slot(
        owner, 20, "08:00", "09:00"
    ) is None


def test_adjacent_tasks():
    owner = make_owner()
    assert Scheduler().find_next_available_slot(
        owner, 30, "09:00", "09:30"
    ) == "09:00"


def test_invalid_duration():
    with pytest.raises(ValueError):
        Scheduler().find_next_available_slot(
            make_owner(), 0
        )
