# FP PROJECT 08 = To-Do List App

print("📋 Welcome to your To-Do List App!")

tasks = []

while True:
print("\n--- MENU ---")
print("1. Add a Task")
print("2. View Tasks")
print("3. Delete a Task")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    task = input("Enter the task: ")
    tasks.append(task)
    print("✅ Task added!")

elif choice == "2":
    print("\\n📝 Your Tasks:")
    if len(tasks) == 0:
        print("No tasks yet. ")

    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

elif choice == "3":
    if len(tasks) == 0:
        print("🚫 No tasks to delete.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"❌ Task '{removed}' removed.")
            else:
                print("❗ Invalid task number.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

elif choice == "4":
    print("👋 Exiting To=Do List App. Goodbye!")
    break

else:
    print("❗ Invalid choice. Please try again.")
