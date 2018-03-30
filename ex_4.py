userNumber = int(input("Enter number: "))

result = []

numberList = list(range(1, userNumber+1))

for num in numberList:
    if userNumber%num == 0:
        result.append(num)

print(result)
