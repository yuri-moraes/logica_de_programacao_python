"""
Contador usando loop, condiconais, truthy e falsey.
"""
plus = 0
quant = 0
number = 0

while True:
    number = int(input("Enter a number: "))
    if number < 0:
        continue
    if not number:
        break
    plus += number
    quant += 1
avarage = plus / quant
print(f"Avarage of the recieved numbers: {avarage}")
