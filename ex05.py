first_value = int(input("Hey, please enter the first value: "))
second_value = int(input("Hey, please enter the second value: "))

if first_value == second_value:
    new_value = print("Oops! These values are equal. Please enter a different value: ")

first_value = int(input("Please enter the first value again: "))
second_value = int(input("Please enter the second value again: "))

if first_value > second_value:
    print(
        f"The first value {first_value} is greater than the second value {second_value}. I knew it!"
    )
else:
    print(
        f"The second value {second_value} is greater than the first value {first_value}. I knew it!"
    )

print(
    "Sorry for these questions. I know they are silly, but I need to practice my programming."
)
