import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal+")
st.write("Your smart pet care planning assistant.")

# Keep Python objects across Streamlit reruns.
if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        name="Alejandra",
        available_minutes=120
    )

owner = st.session_state.owner

# OWNER INFORMATION
st.header("👤 Owner Information")

with st.form("owner_form"):
    owner_name = st.text_input(
        "Owner name", value=owner.name
    )
    available_time = st.number_input(
        "Available minutes per day",
        min_value=0,
        value=owner.available_minutes
    )
    save_owner = st.form_submit_button("Save Owner")

if save_owner:
    owner.name = owner_name.strip()
    owner.available_minutes = int(available_time)
    st.success("Owner information saved!")

# ADD PET
st.header("🐶 Add a Pet")

with st.form("pet_form", clear_on_submit=True):
    pet_name = st.text_input("Pet name")
    species = st.selectbox(
        "Species", ["Dog", "Cat", "Other"]
    )
    age = st.number_input(
        "Age", min_value=0, max_value=40
    )
    add_pet = st.form_submit_button("Add Pet")

if add_pet:
    if pet_name.strip():
        pet = Pet(
            name=pet_name.strip(),
            species=species,
            age=int(age)
        )
        owner.add_pet(pet)
        st.success(f"{pet.name} added successfully!")
    else:
        st.error("Please enter a pet name.")

# PET LIST
if owner.pets:
    st.subheader("My Pets")
    for pet in owner.pets:
        st.write(f"🐾 {pet.name} - {pet.species}, age {pet.age}")
else:
    st.info("Add your first pet to get started.")

# ADD TASK
st.header("📋 Add Care Task")

if owner.pets:
    with st.form("task_form", clear_on_submit=True):
        pet_index = st.selectbox(
            "Select pet",
            range(len(owner.pets)),
            format_func=lambda i: owner.pets[i].name
        )
        task_name = st.text_input("Task name")
        duration = st.number_input(
            "Duration (minutes)",
            min_value=1,
            max_value=240,
            value=20
        )
        priority_label = st.selectbox(
            "Priority", ["Low", "Medium", "High"]
        )
        start_time = st.text_input(
            "Start time (HH:MM, optional)",
            placeholder="08:00"
        )
        add_task = st.form_submit_button("Add Task")

    if add_task:
        from datetime import datetime

        valid_time = True
        if start_time.strip():
            try:
                datetime.strptime(start_time.strip(), "%H:%M")
            except ValueError:
                valid_time = False

        if not task_name.strip():
            st.error("Please enter a task name.")
        elif not valid_time:
            st.error("Use HH:MM format, for example 08:00.")
        else:
            priorities = {
                "Low": 1,
                "Medium": 2,
                "High": 3
            }
            task = Task(
                name=task_name.strip(),
                duration=int(duration),
                priority=priorities[priority_label],
                start_time=start_time.strip() or None
            )
            owner.pets[pet_index].add_task(task)
            st.success("Task added successfully!")

    st.subheader("Current Tasks")
    task_rows = []

    for pet, task in owner.get_all_tasks():
        task_rows.append({
            "Pet": pet.name,
            "Task": task.name,
            "Duration": task.duration,
            "Priority": task.priority,
            "Time": task.start_time or "Flexible",
            "Completed": task.completed
        })

    if task_rows:
        st.dataframe(task_rows, use_container_width=True)
    else:
        st.info("No care tasks added yet.")

# GENERATE SCHEDULE
st.header("📅 Today's Schedule")

if st.button("Generate Schedule"):
    scheduler = Scheduler()
    result = scheduler.generate_plan(owner)

    if result["scheduled"]:
        scheduled_items = sorted(
            result["scheduled"],
            key=lambda item: item[1].start_time or "99:99"
        )
        for pet, task in scheduled_items:
            time = task.start_time or "Flexible"
            st.write(
                f"**{time} | {pet.name}: {task.name}** "
                f"({task.duration} min, priority {task.priority})"
            )
    else:
        st.warning("No tasks could be scheduled.")

    st.write(
        f"Remaining time: {result['remaining_minutes']} minutes"
    )

    if result["deferred"]:
        st.subheader("Deferred Tasks")
        for pet, task in result["deferred"]:
            st.write(
                f"{pet.name}: {task.name} - "
                "Not enough available time"
            )

    conflicts = scheduler.detect_conflicts(
        result["scheduled"]
    )
    if conflicts:
        st.warning(
            f"{len(conflicts)} scheduling conflict(s) detected."
        )
    else:
        st.success("No time conflicts detected!")
