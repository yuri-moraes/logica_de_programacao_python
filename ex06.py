math = float(input("Hey, what is your note on Math my son?\n R: "))
english = float(input("Okay, now what is your note on English? \n R: "))
history = float(input("And history my little? \n R: "))

if math and english and history >= 7:
    print("Nice man! You are qualificate to pass the next level baby!")
else:
    print(
        "Hehe, you are qualificate to be in the floor screaming for help! You are reproved!"
    )
