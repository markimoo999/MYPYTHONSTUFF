import random
i = 0
score = 0
othscore = 0
print ("let's play rock paper scissors!")
while i<5:
    options = ["rock", "paper", "scissors"]
    computer= random.randint(0,2)
    comChoice = options[computer]
    print( comChoice)
    player = input("rock, paper, scissors,\n")
    if comChoice==player:
        print ("tie")
    elif player == "rock" and comChoice=="paper" or player=="scissors" and comChoice=="rock" or player == "paper" and comChoice=="scissors":
        print ("you lose")
        othscore = othscore + 1
        score = score - 1
    elif (player == "rock" and comChoice=="scissors" or player=="scissors" and comChoice=="paper" or player == "paper" and comChoice=="rock"):
        print ("you win")
        score = score + 1
        othscore = othscore - 1
    i =i+1
print( "i'm done. your score was ", score, " and my score was ", othscore,".")
    
            
            
        
    
            
    
