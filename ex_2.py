number = int(input("Enter number: "))

modulo = number%2

if modulo == 0: print("Given number is even")
elif modulo == 1: print("Given number is odd")
if number%4 == 0 : print("Given number is multiple of 4")

num = int(input("Enter another number: "))
check = int(input("Enter dividing number: "))

if num % check == 0: print(num, "divides evenly by", check)
else: print(num, "doesn't divide evenly by", check)
