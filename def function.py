# def dalle(marks1,marks2,marks3,marks4,marks5,marks6,marks7,marks8,marks9,marks10,marks11,marks12):
#     a=((marks1+marks2+marks3+marks4+marks5+marks6+marks7+marks8+marks9+marks10+marks11+marks12)/1100)*100
#     print("najeed youre percentage is",a)
# dalle(90,55,99,66,66,70,99,99,66,66,77,80)
     



# def salam(name):
#     print("asslamokalekum", name)
# salam("haris")




# def add(a, b):
#     return a + b
# print(add(7,7))
# print(add(20,30))




# def add(a , b):

#     return a + b


# print(add(5, 3))



# print(subtract(10, 4))  # 6
# print(multiply(6, 7))   # 42
# print(divide(8, 2))     # 4
# print(divide(5, 0))     # Division not possible



# import random   # random module import

# # computer random number choose karega 1 se 10 ke darmiyan
# secret = random.randint(1, 10)

# while True:
#     # user se input lena
#     guess = int(input("1 se 10 ke darmiyan number guess karo: "))

#     # checking
#     if guess >secret:
#         print("bara number ")
    
#     elif guess < secret:
#         print("Chhota number hai")
#     else:
#         print("Sahi jawab!")

#         break







# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == "+":
#     print("Result:", add(num1, num2))
# elif op == "-":
#     print("Result:", subtract(num1, num2))
# elif op == "*":
#     print("Result:", multiply(num1, num2))
# elif op == "/":
#     print("Result:", divide(num1, num2))
# else:
#     print("Invalid Operator!")










tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("Tasks:", tasks)

    elif choice == "3":
        if tasks:
        # Show tasks with manual numbering
            for i in range(len(tasks)):
                print(i+1, tasks[i])

            rem = int(input("Enter task number to remove: "))
            if rem > 0 and rem <= len(tasks):   # Agar number 0 se bara ho aur list ke andar ho
                del tasks[rem-1]                # Us number wali task delete kar do
                print("Task delete ho gayi!")

            else:
                print("Invalid task number!")
        else:
             print("No tasks to remove!")


    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid option, try again!")