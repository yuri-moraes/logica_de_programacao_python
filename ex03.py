value = float(input("What it's the price of this product? \n R: $ "))
descount = float(
    input("Hey man, what percentage of dicount will be in this price? \n R: ")
)
finalPrice = value - (descount * value / 100)
print(f"So the final price will be ${finalPrice}, right? I want it!")
