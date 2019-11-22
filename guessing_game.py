import math
import random
numbers_list = []
for index in range(10):
    numbers_list.append(random.randint(1, 99))
    guess = int(input("Enter an integer from 1 to 99: "))
    while numbers_list[index] != guess:
        if guess < numbers_list[index]:
            print("guess is low")
            guess = int(input("Enter an integer from 1 to 99: "))
        elif guess > numbers_list[index]:
            print("guess is high")
            guess = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")

numbers_list_two = []
for index in range(10):
    numbers_list_two.append(random.randint(1, 49))
    guess = int(input("Enter an integer from 1 to 49: "))
    while numbers_list_two[index] != guess:
        if guess < numbers_list_two[index]:
            print("guess is low")
            guess = int(input("Enter an integer from 1 to 49: "))
        elif guess > numbers_list_two[index]:
            print("guess is high")
            guess = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")


