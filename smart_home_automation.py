# CodeOrbit IoT Internship - Task 4
# Smart Home Lighting Automation

def smart_light(motion):
    if motion == 1:
        print("Motion detected!")
        print("Smart Light: ON")
    else:
        print("No motion detected.")
        print("Smart Light: OFF")


print("SMART HOME LIGHTING AUTOMATION")
print("Enter 1 for motion detected")
print("Enter 0 for no motion")
print("Enter q to quit")

while True:
    choice = input("\nEnter your choice: ")

    if choice == "1":
        smart_light(1)
    elif choice == "0":
        smart_light(0)
    elif choice.lower() == "q":
        print("Automation stopped.")
        break
    else:
        print("Invalid input. Please enter 1, 0, or q.")
