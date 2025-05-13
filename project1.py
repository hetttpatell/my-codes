
import random

# computerchoice  = random.randint(-1,1)

# # print(computerchoice)

# userchoice = input("Enter your choice of the game : ")

# gamelist= {"rock" : 1, "paper" : 0, "scissors" :-1}

# userinput = gamelist[userchoice]

# print(f"your input {userinput}  vs   computer input {computerchoice}")
# print("Result is : ")

userwin = 0
computerwin = 0

if(userwin == 5 or computerwin ==5):
    
    if(userwin > computerwin):
        print("Congratulations You win !")
    else:
        print("Computer wins !")    
else:    
    for i in range(10):
        computerchoice  = random.choice([-1, 0, 1])

        # print(computerchoice)

        userchoice = input("Enter your choice of the game : ")

        gamelist= {"rock" : 1, "paper" : 0, "scissors" :-1}

        userinput = gamelist[userchoice]

        print(f"your input {userinput}  vs   computer input {computerchoice}")
        print("Result is : ")

        userwin = 0
        computerwin = 0 

        if(computerchoice == userinput):
            print("DRAW !")

        else:
            if(computerchoice == 1 and userinput == 0):
                print("you win.")
                userwin = +1
                

            elif(computerchoice == 1 and userinput == -1):
                print("you loose.") 
                computerwin = +1
            

            elif(computerchoice == 0 and userinput == -1):
                print("you win.")
                userwin = +1
                

            elif(computerchoice == 0 and userinput == 1):
                print("you loose.")  
                computerwin = +1  
                

            elif(computerchoice == -1 and userinput == 0):
                print("you loose.") 
                computerwin = +1
                

            elif(computerchoice == -1 and userinput == 1):
                print("you win.") 
                userwin = +1 
                

            else:
                print("Inappropriate input")
            

    print(userwin)
    print(computerwin)

            