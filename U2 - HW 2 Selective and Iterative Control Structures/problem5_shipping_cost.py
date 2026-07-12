# Problem 5 - Shipping Cost Calculator
# HW 2 - U2 - Selective and Iterative Control Structures
#
# Rate table:
#                     weight <= 5 kg   weight > 5 kg
# distance <= 100 km     $50.00 MXN      $80.00 MXN
# distance >  100 km    $120.00 MXN     $200.00 MXN

# INPUT
total = 0.0     # accumulator for the total shipping cost

entry = input("Enter package weight in kg (or 'exit' to finish): ")

while entry != "exit":
    weight = float(entry)
    distance = float(input("Enter distance in km: "))

    # PROCESS
    if distance <= 100:
        if weight <= 5:
            cost = 50.00
        else:
            cost = 80.00
    else:
        if weight <= 5:
            cost = 120.00
        else:
            cost = 200.00

    total = total + cost

    # OUTPUT
    print(f"Shipping cost: ${cost:.2f} MXN")

    entry = input("Enter package weight in kg (or 'exit' to finish): ")

print(f"Total: ${total:.2f} MXN")
