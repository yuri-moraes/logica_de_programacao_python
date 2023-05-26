days = int(input("Enter a quantity of days: "))
hours = int(input("Enter a quantity of hours: "))
minutes = int(input("Enter a quantity of minutes: "))
seconds = int(input("Enter a quantity of seconds: "))
days *= 86400
hours *= 3600
minutes *= 60
seconds += days + hours + minutes
print(f"The transition of these dates in seconds will be {seconds} seconds on total.")
