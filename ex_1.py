import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
number = int(input("Enter random number: "))
date = datetime.datetime.now().strftime("%Y")
year = 100 - age + int(date)

for x in range(0, number):
    print("{} in {} you will turn 100 years old".format(name, year))
