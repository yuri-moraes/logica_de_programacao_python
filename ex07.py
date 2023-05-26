menu = int(input("What do you want to buy?\n1 - Apple;\n2 - Orange;\n3 - Banana.\nR: "))

if menu == 1:
    quantity = int(input("How much apples do you want buy?\n R:"))
    value = quantity * 2.30
elif menu == 2:
    quantity = int(input("How much oranges do you want buy?\n R:"))
    value = quantity * 3.60
elif menu == 3:
    quantity = int(input("How much bananas do you want buy?\n R:"))
    value = quantity * 1.85
else:
    print("Invalid menu option!")
    exit()

print(f"So pay me ${value:.2f} and you get it!")
