"""
Este é um exemplo de módulo Python.
Ele demonstra o uso de loops e cálculos de tabuada.
"""
number = int(input("Enter a number value: "))

i = 0
while i <= 10:
    calc = number * i
    print(f"{number} x {i} = {calc}")
    i += 1

print("Finished")
