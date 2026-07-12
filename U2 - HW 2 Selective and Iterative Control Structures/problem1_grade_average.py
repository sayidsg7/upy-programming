# Problem 1 - Grade Averaging System
# HW 2 - U2 - Selective and Iterative Control Structures

# INPUT
total = 0.0        # accumulator for the sum of grades
count = 0          # counter of grades entered

entry = input("Enter a grade (or 'done' to finish): ")

# PROCESS
while entry != "done":
    grade = float(entry)
    total = total + grade
    count = count + 1
    entry = input("Enter a grade (or 'done' to finish): ")

# OUTPUT
if count == 0:
    print("No grades entered. Please enter at least one grade.")
else:
    average = total / count
    if average >= 7.0:
        print(f"Average: {average:.2f} — Passed")
    else:
        print(f"Average: {average:.2f} — Failed")
