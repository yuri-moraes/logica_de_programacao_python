print("Welcome to the Restaurant's Yuri Nogueira de Moraes")

# Products table with codes, names, and prices
products = {
    100: ("Hot Dog", 9.00),
    101: ("Double Hot Dog", 11.00),
    102: ("X-Egg", 12.00),
    103: ("X-Salad", 13.00),
    104: ("X-Bacon", 14.00),
    105: ("X-Everything", 17.00),
    200: ("Soda Can", 5.00),
    201: ("Iced Tea", 4.00),
}

# Print the products table
print("-----------------------------------------------")
print("Product Code\tProduct Name\t\tPrice")
print("-----------------------------------------------")
for code, (name, price) in products.items():
    print(f"{code}\t\t{name:<25}${price:.2f}")
print("-----------------------------------------------")

# Dictionary to store customer orders
orders = {}

while True:
    # Request the desired product code
    code = int(input("Enter the product code: "))

    # Check if the code is valid
    if code in products:
        quantity = int(input("Enter the desired quantity: "))
        if code in orders:
            orders[code] += quantity
        else:
            orders[code] = quantity
    elif code == 0:
        # If the code is 0, the program finish
        break
    else:
        # If the code is invalid, display an invalid option message and continue the loop
        print("Invalid option!")
        continue

    # Ask if the customer wants to place more orders
    continue_order = input("Do you want to order anything else? (Y/N): ")
    if continue_order.upper() != "Y":
        break

# Calculate the total value of the order
TOTAL = 0
for code, quantity in orders.items():
    if code in products:
        product_price = products[code][1]
        TOTAL += product_price * quantity

print(f"Total amount to be paid: $ {TOTAL:.2f}")
