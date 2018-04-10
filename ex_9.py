import random

numberToFind = random.randint(1, 9)
userText = input("Enter numer or 'quit' to exit: ")
counter = 1

while not userText == 'quit':
    if int(userText) == numberToFind:
        print("You won in {0} try!".format(counter))
        break
    elif int(userText) > numberToFind:
        print("To high")
        counter+=1
    elif int(userText) < numberToFind:
        print("To low")
        counter+=1

    userText = input("Enter name or 'quit' to exit: ")
    