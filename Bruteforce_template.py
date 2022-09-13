from logging.config import stopListening
from multiprocessing.resource_sharer import stop
import random
import itertools
import string
import time
import os

character = "0123456789abcdefghijklmnopqrstuvwxyz"
chars = string.ascii_lowercase + string.digits
value = ""
printcounter = 0
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

how_often_print = input("How often should I print? (1 = 1 million): ")
second_printcounter = int(how_often_print) * 1000000

while guess != password: 
    if int(which_one) > 0:
        guess = random.choices(character_list,k=len(password))
        guess = "".join(guess)
        if printcounter == second_printcounter:
            print(guess, attempts)
            printcounter = 0
        attempts += 1
        printcounter += 1
        if guess == password:
            attempts = attempts - 1
            print(text.format(guess, attempts))
            exit()
            
    if int(which_one) > 1:
        for password_length in range(1, 9):
            for guess in itertools.product(chars, repeat=password_length):
                guess = ''.join(guess)
                if printcounter == second_printcounter:
                    print(guess, attempts)
                    printcounter = 0
                attempts += 1
                printcounter += 1
                if guess == password:
                    attempts = attempts - 1
                    print(text.format(guess, attempts))
                    exit()