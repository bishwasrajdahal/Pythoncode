print("Hello User!! Let's play guessing Game")
user = input("write the value from 0 to 10")
user_guess = int(user)
from random import random
computer_choice=randint(1,10)
if user_guess>computer_choice:
    print("User won the Game")
elif user_guess<computer_choice:
    print("Computer won the game!")
else:
    print("Game becomes draw!!")