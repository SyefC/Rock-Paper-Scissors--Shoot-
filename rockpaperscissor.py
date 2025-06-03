import random
import os

attemps = 0

while True:
 player = 0
 opponent = 0

 arr = ["rock","paper","scissors"]
 o = random.choice(arr)
 a = input("Choose Rock, Paper or Scissors: ").lower()
 player = arr.index(a)
 opponent = arr.index(o)

 choices = player % 3
 choice = opponent % 3
 if(choices > choice):
    print("\033[32mYou WIN!\n\033[0m\n")
    print(f"Your Attemps {attemps}")
    print(f"Opponent chose: {arr[opponent]}")
    print(f"You chose {arr[player]}")
    break
 elif(choices == choice):
    print("Its A TIE!\n\n")
    print(f"Opponent chose: {arr[opponent]}")
    print(f"You chose {arr[player]}")
 else:
   print("\033[31mOpponent WIN!\n\033[0m\n")
   print(f"Opponent chose: {arr[opponent]}")
   print(f"You chose {arr[player]}")
attemps += 1