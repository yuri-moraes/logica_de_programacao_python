"""
Calculadora usando iterador e contador com loop
"""
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
CALC = 0
i = 1

for i in range(i, x + 1):
    i += 1
    CALC += y

print(f"{x} x {y} = {CALC}")
