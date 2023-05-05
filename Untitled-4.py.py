import random
while True:
    a = (random.randint(1 , 6))
    print(a)
    if a == 6 :
        print(" You have another chance ;) ")
        random.randint(1 , 6)
    else:
        break