'''
Created on Sep 15, 2018

 

@author: ITAUser

'''

 

 

 

 

#Loops the entire game

keepPlaying = True

while(keepPlaying):

    print("Welcome to Rock Paper Scissors!")

    print("Best two out of three. Press 'q' to quit. ")

   

    # 1 = Rock

    # 2 = Scissors

    # 3 = Paper

           

            #Selects a random integer between 1 and 3

    import random


  #sets each player's initial score to zero 
    humanScore = 0

    cpuScore = 0
    
    #loop that repeats each round until the human or cpu score 2 points
    while(humanScore < 2 and cpuScore < 2):
        cpuChoice = random.randint(1,3)
    
        #asks user to select an option
        choice = input("Please choose(Rock, Paper, Scissors): ")
    
      
    
        #checks if user wants to quit
        if(choice == 'q' or choice == 'Q'):
    
            keepPlaying = False
    
            break
    
       
    
        #checks for a draw
    
        elif((choice.lower()== 'rock' and cpuChoice == 1)
             or (choice.lower() == 'scissors' and cpuChoice == 2)
             or (choice.lower() == 'paper' and cpuChoice == 3)):
            print("DRAW!")
            print("Human: " + str(humanScore) + "CPU: " + str(cpuScore))
    
            
    
       #checks if human wins     
        elif((choice.lower() == 'rock' and cpuChoice == 2)
             or (choice.lower() == 'scissors' and cpuChoice == 3)
             or (choice.lower() == 'paper' and cpuChoice == 1)):
            humanScore = humanScore + 1
            print("Human: " + str(humanScore) + "CPU: " + str(cpuScore))       
    
             
    
       #checks if cpu wins
        elif((choice.lower()== 'rock' and cpuChoice == 3)
             or (choice.lower() == 'scissors' and cpuChoice == 1)
             or (choice.lower() == 'paper' and cpuChoice == 2)):
            cpuScore = cpuScore + 1
            print("Human: " + str(humanScore) + "CPU: " + str(cpuScore))
        else:
            print("Not an Option, Try Again.")    
      
print("Thanks for Playing!")
#These two conditions check who won the game
if(humanScore == 2):
    print("You WON!!!")
elif(cpuScore == 2):
    print("You LOSE!!!")
#This prints the final score 
print("Human: " + str(humanScore) + "CPU: " + str(cpuScore))