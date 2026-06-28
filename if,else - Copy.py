# compairesen opretersen ka istmal hoga !=
# age=11
# if age== 18:
#     print("pese mere hain")
# else:
#     print("ye paise mere nhi hain")

# iske zaery input kaise kren
# a=(input("eneter youre going suchwation : "))
# print("you rowt",a)
# if a=="right":
#     print("so you go right")

# elif a=="lift":
#      print(" so you go lift")

# elif a=="baek":
#     print("so you go baek")

# elif a=="go":
#     print("so go")

# else:
#     print("i dont under sdent")
# # def game():
name=(input("enter your name:"))
cilass=int(input("ennter your cilass name:"))
# marks=int((input("enter your marks :")))
schol=(input("enter youre school name "))
subjact=(input("enter your faverit subjact name"))
paste=(input("enter youre laste school name"))
persentag=marks/600*100
# print(persentag)
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
    

# b=input(" are you rady? ")



while True:
    b=input(" are you rady? ")
    if b== "not":
     print("loop is anded") 
     break
    elif b== "yes":
     print("loop is rady")
     c=input("You can only ask abuot three peoples, Ikram, Saleem, and Salman :")
     if c== "who is ikram": 
       print("His name is Ikram. He is an Islamic scholar (Alim) and also a Hafiz of the Holy Quran." 
         "He has dedicated his life to the knowledge and service of Islam. Along with his religious education,"
         "he is currently enrolled in an Arabic-English course to improve his language skills and communication"
         "For the past one year, he has been living in Guromander. This place has provided him with a peaceful" 
         "environment where he can continue his studies and religious activities. His aim is to spread the "
         "knowledge of the Quran and Sunnah and serve the Muslim community through education and guidance.")
     elif c== "who is saleem":
         print("Saleem is an Islamic scholar (Alim-e-Deen) and a Hafiz of the Holy Quran. He lives near Shahzada Masjid, " 
          "close to the Guromander area. He has dedicated his life to the service of Islam through teaching, preaching, and " 
          "guiding people in religious matters"
          "Along with his religious responsibilities, he continues to increase his knowledge to better serve the community."
          "He strongly believes that religious education is the foundation of a peaceful and successful life. He tries his best"
          "to spread the true teachings of Islam with wisdom and kindness."
          "Living in an area like Guromander gives him the opportunity to connect with people from different walks of life and"
          "help them understand the importance of faith, prayer, and good character. May Allah accept his efforts and keep him "
          "firm on the path of truth.")
     elif c==("who is salman"):
          print("Salman is a well-learned Islamic scholar who has devoted himself to the noble cause of spreading religious awareness." 
          "With deep knowledge of the Quran and Sunnah, he serves his community through insightful teaching and sincere guidance. His calm" 
          "nature, respectful manners, and thoughtful speech make him a beloved figure among students and neighbors alike."
          "Residing in Manzoor Colony, Salman remains actively involved in religious gatherings, teaching circles, and youth " 
          "mentorship. His passion for learning and teaching reflects in his disciplined lifestyle and his continuous efforts" 
          "to guide people toward righteousness."
          "His presence is a source of inspiration for many, and his role as a teacher, mentor, and servant of deen is deeply valued."
          "May Allah continue to bless him with wisdom, strength, and acceptance in His service.")
    else:
     print("I am unable to respond.")