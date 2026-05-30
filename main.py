import json
import random
from datetime import datetime
with open("tips.json", "r") as file:
    data = json.load(file)

name = input("Enter your name: ")
print("\nWelcome,", name)
print("This is your Smart Student Assistant")
print("\nMenu")
print("1. Generate Study Tips")
print("2. Generate Motivation Quote")
print("3. Display Current Date & Time")
print("4. Exit")
choice = input("Enter your choice (1-4): ")
if choice == "1":
    tip = random.choice(data["tips"])
    print("\nStudy Tip:")
    print(tip)

    with open("output.txt", "a") as file:
        file.write("Study Tip:\n")
        file.write(tip + "\n\n")
elif choice == "2":
    quote = random.choice(data["quotes"])
    print("\nMotivation Quote:")
    print(quote)

    with open("output.txt", "a") as file:
        file.write("Motivation Quote:\n")
        file.write(quote + "\n\n")
elif choice == "3":
    current_time = datetime.now()
    print("\nCurrent Date and Time:")
    print(current_time)

    with open("output.txt", "a") as file:
        file.write("Current Date and Time:\n")
        file.write(str(current_time) + "\n\n")
elif choice == "4":
    print("Thank you for using Smart Student Assistant.")
else:
    print("Invalid choice!")
