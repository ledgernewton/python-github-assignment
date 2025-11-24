"""
Study Time Tracker

This simple program asks the user how many hours they studied today,
then estimates how many hours they are on track to study this week.
It includes basic error handling for non-numeric input.
"""

# 1. Welcome message
print("Welcome to my Python study time tracker!")

# 2. Ask the user for input
hours_today = input("How many hours did you study today? ")

# 3. Try to convert input to a number safely
try:
    hours_today = float(hours_today)
except ValueError:
    print("Please enter a valid number for hours (for example: 1.5).")
    exit()

# Optional: check for negative numbers
if hours_today < 0:
    print("Study hours cannot be negative. Please run the program again.")
    exit()

# 4. Perform the calculation (estimate weekly hours)
weekly_hours = hours_today * 7

# 5. Display the result clearly
print(f"If you keep this pace, you will study about {weekly_hours:.1f} hours this week.")
print("Nice work staying on top of your study time!")
