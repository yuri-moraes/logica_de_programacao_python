"""
Contadora de cédulas
"""

while True:
    value = int(input("Enter a integer value:\n $"))

    if value > 100:
        hundred = value // 100
        value -= hundred * 100
        print(f" {hundred} bills of $100")
    if value > 50:
        fifty = value // 50
        value -= fifty * 50
        print(f" {fifty} bills of $50")
    if value > 20:
        tweny = value // 20
        value -= tweny * 20
        print(f" {tweny} bills of $20")
    if value > 10:
        ten = value // 10
        value -= ten * 10
        print(f" {ten} bills of $10")
    if value > 5:
        five = value // 5
        value -= five * 5
        print(f" {five} bills of $5")
    if value:
        one = value
        value -= one
        print(f" {one} bills of $1")
    else:
        print("Finishing Program!")
        break
