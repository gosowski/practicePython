a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = []

num = int(input("Enter number: "))

for number in a:
    if(number < num):
        result.append(number)

print(result)
