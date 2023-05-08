import random
n = int(input("Enter list's lengh : "))
arr = []
while len(arr)<n:
    num = random. randint(1 , 1000)
    if num not in arr:
        arr.append(num)
print(arr)