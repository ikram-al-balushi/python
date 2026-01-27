
import random
print("welcome to scissor, paper,rock, game. ")
print("you have a three options(paper, scissor,rock)")

user_choice=input("enter your choice:").lower()

options=["paper", "scissore"," rock"]
compueter_chice=random.choice(options)
print(f"computer choice:{compueter_chice}")

if compueter_chice==user_choice:
        print("game is tia")
elif compueter_chice=="scissor":
      if user_choice=="paper":
       print("compueter is win")
      else:
         print(" you win")
elif compueter_chice=="rock ":
        if user_choice=="scissor":
           print("compueter is win ")
        else:
            print("you win")
elif compueter_chice=="paper":
       if user_choice=="rock":
        print("compueter is win")
else:
        print("you win")
   






sa=[2,34,65,99,76,00,56,98,99,65,76,32,90,45,66]
# sa.insert(4,54)
# sa.pop(3)
# sa.append(5)
# sa.reverse()
# sa.remove(65)

print(sa)