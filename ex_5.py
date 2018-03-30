import random

a = []
b = []

for i in range(15):
    a.append(random.randrange(1, 101,1))

for i in range(20):
    b.append(random.randrange(1,101,1))

# print(a)
# print(b)

result = []
for number in a:
    for num in b:

        if number == num:
            result.append(number)

print(set(result))
