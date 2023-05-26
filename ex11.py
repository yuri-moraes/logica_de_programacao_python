"""
Contador usando loop e condicionais
"""

initial_value = int(input("Enter a initial value: "))
final_value = int(input("Enter a final value: "))

integer_numbers = 0
sum_integer = 0
odd_numbers = 0
sum_odd = 0
even_numbers = 0
sum_even = 0
avarage = 0

for i in range(initial_value, final_value + 1):
    if i > 0:
        integer_numbers += 1
        sum_integer += i
    if i % 2 == 0:
        odd_numbers += 1
        sum_odd += i
    else:
        even_numbers += 1
        sum_even += i

total = final_value - initial_value
avarage = total / i
odd_avarage = sum_odd / odd_numbers
even_avarage = sum_even / even_numbers

print(f"Integer and positive numbers: {integer_numbers}")
print(f"Odd Numbers: {odd_numbers}")
print(f"Odd values avarage: {odd_avarage}")
print(f"Even numbers: {even_numbers}")
print(f"Even values avarage: {even_avarage}")
print(f"Positive values Avarage: {avarage:.2f}")
