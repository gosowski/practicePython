def numberToCheck():
    return int(input("Enter number: "))

def isPrime(num):
    check = True
    for i in range(2, num):
        if num%i == 0:
            check = False
            break
    return check

a = numberToCheck()
b = isPrime(a)

if b:
    print("Number {0} is prime number".format(a))
else:
    print("Number {0} is NOT prime number".format(a))