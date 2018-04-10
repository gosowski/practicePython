def num():
    return int(input("Enter number of elements: "))

def fillList(num):
    result = []
    for i in range(num):
        result.append(input("Enter value of {0} element: ".format(i)))
    return result

number = num()
objList = fillList(number)
print(objList)

objList = set(objList)
objList = list(objList)
print(objList)

