import random as h
game = ["rock","paper","scissor"]
selectedname = h.choice(game)
while(True):
    a = input("Enter rock,paper,scissor:")
    print("you chose",a,".computer chose",selectedname)
    if a == "rock" and selectedname == "paper" or a == "scissor" and selectedname == "rock" or a == "paper" and selectedname == "scissor":
        print("computer wins")
    elif a == "rock" and selectedname == "rock" or a == "paper" and selectedname == "paper" or a == "scissor" and selectedname == "scissor":
        print("its a tie")
    else:
        print("you win")
    b = int(input("Do u want to stop!press 1 to stop,2 to continue "))
    if b == 2:
        continue
    else:
        print("game over") 



    
