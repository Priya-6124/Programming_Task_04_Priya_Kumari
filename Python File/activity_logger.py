from datetime import datetime

def create_log(activity):

    current_time = datetime.now()

    with open("activity_log.txt", "a") as file:

        file.write(f"Date: {current_time.date()}\n")
        file.write(f"Time: {current_time.strftime('%H:%M:%S')}\n")
        file.write("Program Name: Activity Logger\n")
        file.write(f"User Activity: {activity}\n")
        file.write("-" * 40 + "\n")

activity = input("Enter Activity: ")

create_log(activity)

print("Activity Logged Successfully!")
