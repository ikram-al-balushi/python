# compairesen opretersen ka istmal hoga !=,==
age=11
if age == 18:
    print("pese mere hain")
else:
    print("ye paise mere nhi hain")

# iske zaery input kaise kren
a=(input("say your command: "))
print("enter your number",a)
if a=="right":
    print("go right")

elif a=="lift":
     print("go lift")

elif a=="baek":
    print("go baek")

elif a=="sedha":
    print("bilkull sedha")

else:
    print("i dont under sdent")




name=(input("enter your name:"))
cilass=int(input("ennter your cilass name:"))
marks=int((input("enter your percntage.")))
schol=(input("enter youre school name "))
subjact=(input("enter your faverit subjact name"))
paste=(input("enter youre laste school name"))
persentag=marks/600*100
print(persentag)
print(f"may name is {name}\n may cilas name is :{cilass}\n may last school name {schol}\n may faverit subjact name is {subjact}\n may laste school name is {paste}\n may percentage is {persentag}")
if persentag>=480:
  print("may gread is A+")
elif marks>=380:
  print("may gret is B+")
elif marks>=280:
  print("may gret is C+")
elif marks>=240:
  print("may gred is D+")
else :
  print("i am fail")
    #  print(f"may name is 1)




