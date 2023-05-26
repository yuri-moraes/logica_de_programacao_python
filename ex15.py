"""
Quantificador de ingressos por idade
idade < 3 == $0 / 3 <= idade <= 12 == $15 / idade > 12 == $30
"""
CONT = 0
ACUM = 0
AGE_ACUM = 0

while True:
    print("-" * 25)
    age = int(input("Enter your age: "))
    AGE_ACUM += age
    people = input(
        "Do you want to calculate the price for one more person? (S/N): "
    ).upper()
    CONT += 1
    if age < 3:
        print("You have a free ticket.")
    elif 3 <= age <= 12:
        print("The ticket price is $15.00")
        ACUM += 15
    elif age > 12:
        print("The ticket price is $30.00")
        ACUM += 30
    if people == "N":
        break

average = AGE_ACUM / CONT

print(
    f"Total of persons registered: {CONT}\nAge average: {average}\nTotal accumulated: ${ACUM:.2f}"
)
