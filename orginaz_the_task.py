# Ask user for tasks (separated by comma and space)
tasks = input("Enter your tasks for today (separate them with ', '): \n").split(", ")

done_tasks = []
not_done_tasks = []

for task in tasks:
    print(f"\nTask: {task}\n")
    finished = input("Did you finish this task? (yes/no): \n ").lower()

    if finished == "yes":
        print("✅ Good job, keep it up!")
        done_tasks.append(task)
    elif finished == "no":
        print("⚠️ Try to complete it today!")
        not_done_tasks.append(task)
    else:
        print(f"🤔 I didn't understand '{finished}', but if you finished your task, good work!\nIf not, try to do it today.")

    print("------------------")

choice = input("Do you want to see a summary of your tasks today? (yes/no): \n ").lower()

if choice == "yes":
    print(f"\n📌 Tasks not done today: {not_done_tasks}")
    print(f"✅ Tasks finished today: {done_tasks}")
