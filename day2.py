print("Welcome to Tip Calculator")
total = input("What is the total bill? ")

tip = input("What percent tip would you like to leave? ")
tip_multiplier = int(tip) / 100
num_of_people = input("how many people are splitting the bill? ")

total_float = int(total)

total_with_tip = ((total_float * tip_multiplier) + total_float
print(total_with_tip)
each = total_with_tip / int(num_of_people)


print(f"Each person should leave {each}")
