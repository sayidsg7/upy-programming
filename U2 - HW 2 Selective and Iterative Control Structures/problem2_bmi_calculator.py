# Problem 2 - BMI Calculator
# HW 2 - U2 - Selective and Iterative Control Structures

# INPUT
entry = input("Enter weight in kg (or 'exit' to finish): ")

while entry != "exit":
    weight = float(entry)
    height = float(input("Enter height in m: "))

    # PROCESS
    bmi = weight / height ** 2

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # OUTPUT
    print(f"BMI: {bmi:.2f} — {category}")

    entry = input("Enter weight in kg (or 'exit' to finish): ")
