#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
 #Create a loop that continues as long as the user wants to play.
 #User can play as many games as they wish.
  play = "Y"
  while play == "Y":
#Randomly choose the computer between 'R', 'P', or 'S'
    player = input("Chooese between (R/P/S): ")
    computer = random.choice(["R", "P", "S"])
    print("I choose", computer)
    #Prompt the user for their RPS selection
    
#Determine winner and state what happened to the user
   
    if player == computer:
      print("Tie")
      ties = ties + 1
    elif player > computer:
      print("You Won!!!")
      wins = wins + 1
    elif player < computer:
      print("You Suck! ToT")
      losses = losses + 1
#Ask the user if they would like to play again.
    play = input("Play again? (Y/N): ")
  
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
