task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match-case and conditional logic
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that still needs to be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to do it soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task, but it's time-sensitive. Try to make time today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please choose from high, medium, or low.")