print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = bill * (int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100)
people = int(input("How many people to split the bill? "))
total_amount = bill + tip
payables = total_amount / people
print(f"Each person should pay: ${payables:.2f}")
