## NUMBER GUESSING
import random

RandomNum = random.randrange(1,200)
# print(RandomNum)
userInput = int(input("Guess the number:"))

if userInput > RandomNum:
  if userInput > RandomNum:
     print(RandomNum)

     print("The number is too high")
elif RandomNum > userInput:
     print(RandomNum)
     print("The number is too low")

else:
    print(RandomNum)
    print("Yes,you guessed the number")