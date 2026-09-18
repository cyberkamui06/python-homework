print("VOTER ELIGIBILITY CHECK")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ").lower()

is_citizen = citizen == "yes"

if age >= 18 and is_citizen:
    print(f"{name}, you are eligible to vote.")
else:
    print(f"Sorry {name}, you are not eligible to vote because you must be at least 18 years old and be a citizen.")