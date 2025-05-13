import math
import random

randomnumber = random.randint(1,100)

print(randomnumber)
condition = True
userchance = 1
while (condition):
 
 
    print(f"Your guess chance is {userchance}")

    userguess = int(input("Enter your guess : "))
    userchance += 1

    # print(f"Your guess chance is {userchance}")wd

    if(userguess > randomnumber):
        print("Your guess is higher then the actual number. \n")
        

    elif(userguess < randomnumber):
        print("Your guess is lower than the actual number.\n")
       

    elif(userguess == randomnumber):
        print("Congratulations your guess is accurate \n")
        condition = False
       

else:
        print(f"Game over and you take {userchance} to guess the number.")
        