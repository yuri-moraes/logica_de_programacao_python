"""
Calculadora com while
"""

CHOICE = 0

while CHOICE != 5:
    print("-" * 20)
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter de second number: "))
    CHOICE = input(
        "What kind of operation do you want to realize?\n 1 - Addition (+)\n 2 - Subtraction(-)\n 3 - Multiplication(x)\n 4 - Division(/)\n 5 - Leave\n R:"
    )

    if CHOICE == "1" or CHOICE == "+":
        calc = first_number + second_number
        print(f"{first_number} + {second_number} = {calc}")
        continue
    elif CHOICE == "2" or CHOICE == "-":
        calc = first_number - second_number
        print(f"{first_number} - {second_number} = {calc}")
        continue
    elif CHOICE == "3" or CHOICE == "x":
        calc = first_number * second_number
        print(f"{first_number} x {second_number} = {calc}")
        continue
    elif CHOICE == "4" or CHOICE == "/":
        calc = first_number / second_number
        print(f"{first_number} / {second_number} = {calc}")
        continue
    elif CHOICE == "5":
        print("Finishing program...")
        break
    else:
        print("Invalid value!")
        continue
