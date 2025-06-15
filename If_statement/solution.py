# Write code below 💖
Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0
Q1=int(input("Q1) Do you like Dawn or Dusk?\n 1) Dawn\n 2) Dusk\n"))
if Q1==1:
  Gryffindor+=1
  Ravenclaw+=1
elif Q1==2:
  Hufflepuff+=1
  Slytherin+=1
else:
  print("Wrong input.")
Q2=int(input("Q2 When I’m dead, I want people to remember me as:\n1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n"))
if Q2==1:
   Hufflepuff+=2
elif Q2==2:
  Slytherin+=2
elif Q2==3:
  Ravenclaw+=2
elif Q2==4:
  Gryffindor+=2
else:
  print("Wrong input.")
Q3=int(input("Q3) Which kind of instrument most pleases your ear?\n  1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n"))
if Q3== 1:
   Slytherin+=4
elif Q3==2:
  Hufflepuff+=4
elif Q3==3:
  Ravenclaw+=4
elif Q3==4:
  Gryffindor+=4
else:
  print("Wrong input.")

print("Slytherin: ",Slytherin)
print("Hufflepuff: ",Hufflepuff)
print("Ravenclaw: ",Ravenclaw)
print("Gryffindor: ",Gryffindor)
