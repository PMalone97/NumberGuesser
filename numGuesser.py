#The user guesses what number the computer is 'thinking' of from a selected range of values.
from random import randint

x = input("Enter lower value: ")
y = input("Enter upper value: ")
print("{} {}-{}".format("Your range is:",x,y))

randVal = (randint(x,y))

def guess(randVal, count = 1):

    choice = input("Guess the number!: ")
    print("{}: {} ".format("Number of Guesses", count))

    while (choice != randVal):

        if choice < randVal:
            print ('Higher!')

        else:
            print('Lower!')

        choice = input("Guess again: ")
        count += 1
        print("{}: {} ".format("Number of Guesses", count))


guess(randVal)
print("{}: {}".format("Nice work! The number was", randVal))
