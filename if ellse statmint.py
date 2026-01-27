import random
print("welcome to rock, paper, scissors game")
print("Enter yore choice (rock,paper,scissors):")


user_choice=input("youre choice:").lower()

options=["rock","paper","scissors"]
computer_choice=random.choice(options)
print(f"computer choice:{computer_choice}")


if computer_choice==user_choice:
    print("game is tie")
elif user_choice=="rock":
     if computer_choice=="scissors":
         print("youn win")
     else :
         print("computer is win") 
elif user_choice=="scissors":
     if computer_choice=="paper":
          print(" you win")
     else:
          print("computer is win")
elif user_choice=="paper":
     if computer_choice=="rock":
          print("you win")
     else:
          print("computer is win")  
else:
     print("nothing")