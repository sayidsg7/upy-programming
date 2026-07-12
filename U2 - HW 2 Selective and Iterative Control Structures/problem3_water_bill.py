# Problem 3 - Water Bill Calculator
# HW 2 - U2 - Selective and Iterative Control Structures

# INPUT
total = 0.0     # accumulator for the total charge

entry = input("Enter m3 consumed (or 'exit' to finish): ")

while entry != "exit":
    consumption = float(entry)

    # PROCESS
    if consumption <= 10:
        rate = 8.00
    elif consumption <= 20:
        rate = 12.00
    else:
        rate = 18.00

    charge = consumption * rate
    total = total + charge

    # OUTPUT
    print(f"Month charge: ${charge:.2f} MXN")

    entry = input("Enter m3 consumed (or 'exit' to finish): ")

print(f"Total: ${total:.2f} MXN")
