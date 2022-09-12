from logging.config import stopListening
from multiprocessing.resource_sharer import stop
import random
import itertools
import string
import time

character = "0123456789abcdefghijklmnopqrstuvwxyz"
chars = string.ascii_lowercase + string.digits
value = ""
character_list = list(character)
attempts = 0
text = "Password is {}, took {} tries."
password = input("Type a password: ")
guess = ""
a = """
1. Guessing  
2. Guessing in alphabetic order
"""
which_one = input(a)


while guess != password: 
    if int(which_one) > 0:
        guess = random.choices(character_list,k=len(password))
        guess = "".join(guess)
        print(guess, attempts)
        attempts += 1    
        if guess == password:
            attempts = attempts - 1
            print(text.format(guess, attempts))
            exit()
            
    if int(which_one) > 1:
        for password_length in range(1, 9):
            for guess in itertools.product(chars, repeat=password_length):
                guess = ''.join(guess)
                print(guess, attempts)
                attempts += 1
                if guess == password:
                    attempts = attempts - 1
                    print(text.format(guess, attempts))
                    exit()