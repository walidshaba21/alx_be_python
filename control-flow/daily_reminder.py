task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

priority = priority.lower()
time_bound = time_bound.lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task that isn't time bound!")

    case "medium": 
        if time_bound == "yes":
            print("Reminder: '{task}' is a medium priority task do when other major task are completed,it is time bound also.")
        else:
            print("Reminder: '{task}' to be completed, is not time sensitive.")
    case "low":
        if time_bound == "yes":
            print("Note: '{task}' is a low priority task. Consider doing when other time sensitive tasks are done")
        else: 
            print("Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid input entered.")
