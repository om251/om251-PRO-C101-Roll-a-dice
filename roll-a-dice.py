import random
while True:
    respone = input("Do you want to roll a dice? (y/n): ")
    if respone == 'y':
        number = random.randint(1, 6)
    elif respone == 'n':
        print("Goodbye!")
        break
    else:
        print("Invalid input, please try again.")

    if number == 1:
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")

    elif number == 2:  
        print("---------")
        print("|       |")
        print("| O   O |")
        print("|       |")
        print("---------")

    elif number == 3:
        print("---------")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print("---------")

    elif number == 4:
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")

    elif number == 5:
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
    
    elif number == 6:
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")

