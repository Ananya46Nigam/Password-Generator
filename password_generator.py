
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
level= input("What level of password would you like to generate? Easy or hard?").lower()
#Eazy Level - Order not randomised



#Hard Level - Order of characters randomised

letter=""
symbol=""
num="" 

for i in range(1,nr_letters+1):
    letter=letter+random.choice(letters)

for i in range(0,nr_symbols):
    letter=letter+random.choice(symbols)

for i in range(0,nr_numbers):
    letter=letter+random.choice(numbers)


if level=="easy":
    print(letter)
    

elif level=="hard":
    #print(password)
    password=list()

    for i in range(0,len(letter)):
        password.append(letter[i])
        random.shuffle(password)
        result="".join(password)
    print(result)
