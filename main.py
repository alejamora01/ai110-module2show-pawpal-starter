from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Alejandra", 120)

ares = Pet("Ares", "Dog", 3)
milo = Pet("Milo", "Cat", 2)

ares.add_task(Task(
    "Afternoon walk", 30, 2,
    start_time="16:00"
))

milo.add_task(Task(
    "Breakfast", 15, 3,
    start_time="08:00",
    recurrence="daily"
))

ares.add_task(Task(
    "Morning walk", 30, 3,
    start_time="08:10"
))

milo.add_task(Task(
    "Playtime", 20, 1,
    start_time="12:00"
))

owner.add_pet(ares)
owner.add_pet(milo)

scheduler = Scheduler()
all_tasks = owner.get_all_tasks()

print("\nPAWPAL+ | TODAY'S SCHEDULE")
print("-" * 45)

plan = scheduler.generate_plan(owner)

for pet, task in scheduler.sort_by_time(
    plan["scheduled"]
):
    print(
        f"{task.start_time} | {pet.name}: "
        f"{task.name} ({task.duration} min)"
    )

print("-" * 45)
print(
    "Remaining minutes:",
    plan["remaining_minutes"]
)

print("\nFILTER: ARES")
for pet, task in scheduler.filter_tasks(
    all_tasks, pet_name="Ares"
):
    print(pet.name, "-", task.name)

print("\nCONFLICT DETECTION")
conflicts = scheduler.detect_conflicts(
    plan["scheduled"]
)

for first, second in conflicts:
    print(
        f"WARNING: {first.name} overlaps "
        f"with {second.name}"
    )

if not conflicts:
    print("No conflicts detected.")

print("\nRECURRING TASK TEST")

breakfast = milo.tasks[0]
next_task = milo.complete_task(breakfast)

if next_task:
    print("Completed:", breakfast.name)
    print("Next occurrence:", next_task.due_date)
    print("Expected:", date.today().toordinal() + 1)
    print(
        "Recurrence verified:",
        (next_task.due_date - breakfast.due_date).days == 1
    )
