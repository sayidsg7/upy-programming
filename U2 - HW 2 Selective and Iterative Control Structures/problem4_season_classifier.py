# Problem 4 - Season Classifier
# HW 2 - U2 - Selective and Iterative Control Structures

# INPUT
entry = input("Enter a month number 1-12 (or 'exit' to finish): ")

while entry != "exit":
    month = int(entry)

    # PROCESS
    if month < 1 or month > 12:
        result = "Invalid month. Please enter a number between 1 and 12."
    elif month == 12 or month == 1 or month == 2:
        result = "Winter"
    elif month >= 3 and month <= 5:
        result = "Spring"
    elif month >= 6 and month <= 8:
        result = "Summer"
    else:
        result = "Fall"

    # OUTPUT
    print(result)

    entry = input("Enter a month number 1-12 (or 'exit' to finish): ")
