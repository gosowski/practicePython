import random

def generateList():
    nums = int(input("Enter how much numbers you want in list: "))
    numList = random.sample(range(1, 50), nums)
    return numList

def showFirstLast(l):
    #  a = l[0]
    #  l.reverse()
    #  b = l[0]
     return l[0], l[-1]

numbers = generateList()

if len(numbers) > 0:

    a,b = showFirstLast(numbers)

    print("First number in list is {0} last is {1}".format(a, b))
