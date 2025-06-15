# sorting_hat.py
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

# Question 1
q1 = int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))
if q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input.")

# Question 2
q2 = int(input("\nQ2) When I'm dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))
if q2 == 1:
    Hufflepuff += 2
elif q2 == 2:
    Slytherin += 2
elif q2 == 3:
    Ravenclaw += 2
elif q2 == 4:
    Gryffindor += 2
else:
    print("Wrong input.")

# Question 3
q3 = int(input("\nQ3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))
if q3 == 1:
    Slytherin += 4  # Fixed from original code
elif q3 == 2:
    Hufflepuff += 4
elif q3 == 3:
    Ravenclaw += 4
elif q3 == 4:
    Gryffindor += 4
else:
    print("Wrong input.")

# Bonus: Determine winning house
houses = {
    "Gryffindor": Gryffindor,
    "Ravenclaw": Ravenclaw,
    "Hufflepuff": Hufflepuff,
    "Slytherin": Slytherin
}

print("\n=== Results ===")
for house, points in houses.items():
    print(f"{house}: {points}")

max_points = max(houses.values())
winners = [house for house, points in houses.items() if points == max_points]

print("\nThe winning house is..." if len(winners) == 1 else "\nIt's a tie between...")
print(", ".join(winners) + "!")
