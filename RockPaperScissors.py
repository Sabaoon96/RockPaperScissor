import random

print("The Rock Paper Scissors Game\n")

rock = 1
paper = 2
scissors = 3

user = 0

while user != -1:
    print("Choose \n1 for Rock, \n2 for Paper, \n3 for Scissors, \nor \n-1 to Quit!\n")
    user = int(input("Please enter your choice: "))
    computerChoice = random.randint(1,3)

    if user != -1:
        if user == rock:
              print("You chose rock")
        elif user == paper:
              print("You chose paper")
        elif user == scissors:
              print("You choose scissors")
    else:
        break

    
    if computerChoice == rock:
        print("Computer chose rock\n")
    elif computerChoice == paper:
        print("Computer chose paper\n")
    elif computerChoice == scissors:
        print("Computer choose scissors\n")


    if (computerChoice == user):
        print("It's a TIE!!!")
    elif (user == rock and computerChoice == scissors) or (user == paper and computerChoice == rock) or (user == scissors and computerChoice == paper):
        print("You win :)")        
    else:
        print("The computer won :(")
        
