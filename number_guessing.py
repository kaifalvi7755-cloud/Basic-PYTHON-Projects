print("======================================================================================")
print("                                NUMBER GUESSING GAME                                  ")
print("======================================================================================")

import random

num=random.randint(1,10)
user=int(input("enter your guessed number"))

if num==user:
    print("you are right")
else:
    print("you are wrong")