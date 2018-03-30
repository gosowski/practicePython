name = input("Enter your name: ")
age = int(input("Enter your age: "))
number = int(input("Enter random number: "))
year = 100 - age + 2018

for x in range(0, number):
    print("{} in {} you will turn 100 years old".format(name, year))
