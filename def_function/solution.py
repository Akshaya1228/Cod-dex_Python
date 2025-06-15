# Write code below 💖
def welcome():
  print("welcome to McDonald's")
  print("This is the menu\n1) 🍔 Cheeseburger\n2) 🍟 Fries\n3) 🥤 Soda\n4) 🍦 Ice Cream\n5) 🍪 Cookie'")
menu=['🍔 Cheeseburger','🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']
def get_item(n):
  return menu[int(n)-1]
welcome()
n=input("What would you like to orde: ")
if n in ["1", "2", "3", "4", "5"]:
  print(get_item(n))
else:
  print("Invalid")

