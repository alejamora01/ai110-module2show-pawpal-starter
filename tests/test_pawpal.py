from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion():
    task = Task("Feeding", 10, 3)
    assert task.completed is False

    task.mark_complete()
    assert task.completed is True


def test_task_addition():
    pet = Pet("Luna", "Dog", 3)
    task = Task("Walking", 30, 3)

    pet.add_task(task)
    assert len(pet.tasks) == 1


def test_multi_pet_schedule():
    owner = Owner("Alejandra", 60)
    luna = Pet("Luna", "Dog", 3)
    milo = Pet("Milo", "Cat", 2)

    luna.add_task(Task("Walking", 20, 3))
    milo.add_task(Task("Feeding", 10, 2))

    owner.add_pet(luna)
    owner.add_pet(milo)

    result = Scheduler().generate_plan(owner)

    assert len(result["scheduled"]) == 2
    assert result["remaining_minutes"] == 30


def test_priority_sorting():
    owner = Owner("Alejandra", 60)
    pet = Pet("Luna", "Dog", 3)

    pet.add_task(Task("Playtime", 20, 1))
    pet.add_task(Task("Medication", 10, 3))
    owner.add_pet(pet)

    result = Scheduler().generate_plan(owner)

    assert result["scheduled"][0][1].name == "Medication"


def test_time_constraint():
    owner = Owner("Alejandra", 20)
    pet = Pet("Luna", "Dog", 3)

    pet.add_task(Task("Long Walk", 40, 3))
    owner.add_pet(pet)

    result = Scheduler().generate_plan(owner)

    assert len(result["scheduled"]) == 0
    assert len(result["deferred"]) == 1


def test_completed_tasks_excluded():
    owner = Owner("Alejandra", 60)
    pet = Pet("Luna", "Dog", 3)
    task = Task("Feeding", 10, 3)

    task.mark_complete()
    pet.add_task(task)
    owner.add_pet(pet)

    result = Scheduler().generate_plan(owner)

    assert len(result["scheduled"]) == 0
