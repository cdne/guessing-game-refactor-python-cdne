import math
import random
a = []
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
for index in range(10):
    g = int(input("Enter an integer from 1 to 99: "))
    while a[index] != g:
        if g < a[index]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 99: "))
        elif g > a[index]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")

b = []
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
for index in range(10):
    g = int(input("Enter an integer from 1 to 49: "))
    while b[index] != g:
        if g < b[index]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > b[index]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")


