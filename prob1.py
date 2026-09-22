
try:
    age = int(input("Enter the Age: "))

    if 12 <= age <= 18:
        print("Valid Age")
    else:
        print("Invalid Age: Age must be from 12 to 18")


except ValueError:
    print("Invalid input. Please enter a whole number.")
