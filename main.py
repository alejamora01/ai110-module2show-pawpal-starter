from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Alejandra", available_minutes=100)

luna = Pet("Luna", "Dog", 3)
milo = Pet("Milo", "Cat", 2)

luna.add_task(Task(
    "Morning walk", 30, 3,
    category="outdoor", start_time="08:00"
))

luna.add_task(Task(
    "Breakfast", 10, 3,
    category="feeding", start_time="09:00"
))

milo.add_task(Task(
    "Medication", 15, 3,
    category="medication", start_time="08:30"
))

milo.add_task(Task(
    "Playtime", 20, 1,
    category="enrichment", start_time="10:00"
))

owner.add_pet(luna)
owner.add_pet(milo)

scheduler = Scheduler()
result = scheduler.generate_plan(owner)

print("\nPAWPAL+ | TODAY'S SCHEDULE")
print("-" * 45)

for pet, task in result["scheduled"]:
    time = task.start_time or "Flexible"
    print(
        f"{time} | {pet.name}: {task.name} "
        f"({task.duration} min) "
        f"[priority: {task.priority}]"
    )

print("-" * 45)
print(f"Remaining time: {result['remaining_minutes']} minutes")
print(f"Deferred tasks: {len(result['deferred'])}")

conflicts = scheduler.detect_conflicts(
    result["scheduled"]
)
print(f"Time conflicts: {len(conflicts)}")
