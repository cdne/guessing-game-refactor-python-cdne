import math
import random

def guessing_game(random_number_one, random_number_two):
    numbers_list = []
    for index in range(10):
        numbers_list.append(random.randint(random_number_one, random_number_two))
        guess = int(input(f"Enter an integer from {random_number_one} to {random_number_two}: "))
        while numbers_list[index] != guess:
            if guess < numbers_list[index]:
                print("guess is low")
                guess = int(input(f"Enter an integer from {random_number_one} to {random_number_two}: "))
            elif guess > numbers_list[index]:
                print("guess is high")
                guess = int(input(f"Enter an integer from {random_number_one} to {random_number_two}: "))
            else:
                break
        print("you guessed it!")

guessing_game(1,99)
guessing_game(1,49)

