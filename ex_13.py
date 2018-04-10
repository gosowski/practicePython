def askNumber():
    num = int(input("Enter how much fibonacci numbers tou want to print: "))
    return num

def generateFib(num):
    result = []
    if num <= 2:
        for i in range(num):
            result.append(1)
    else:
        result = [1,1]
        for i in range(2,num):
            result.append(result[i-2]+result[i-1])     
    return result

nums = askNumber()
print(generateFib(nums))
