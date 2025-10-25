"""Instructions"""
    #ask the user if they want to generate a password or not
    #if yes ask for password length
    #print password
    #if initial response is no exit program

import string
import random

charchters = list(string.ascii_letters + string.digits + "@Sami-5485!")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(charchters)

    password = []
    
    for y in range(password_length):
        password.append(random.choice(charchters))
    
    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want to generate your password? (Yes/No): ")
if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended!")
    quit()
else:
    print("Invalid input, please rewrite Yes or No")
    quit()
