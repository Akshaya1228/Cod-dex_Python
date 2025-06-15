import random
symbols=['🍒',' 🍇', '🍉', '7️⃣']

def play():
  results=random.choices(symbols,k=3)
  print(results[0],"|",results[1],"|",results[2])
  if results==['7️⃣','7️⃣','7️⃣']:
      print("Jackpot! 💰")
  else:
      print("Thanks for playing!")
  
while True:  
  play()
  p=input("do you want to continue to play again:")
  if p!="Y":
      print("Thanks for playing")
      break