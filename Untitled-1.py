a = int(input("Enter side a : "))
b = int(input("Enter said b : "))
c = int(input("Enter said c : "))
if a + b > c and a + c > b and c + b > a:
    print("you can have a triangle")
else:
    print("you con not have a triangle")