name = input("Enter your full name : ")
a = float(int(input("Enter your score : ")))
b = float(int(input("Enter your score : ")))
c = float(int(input("Enter your score : ")))
average = (a + b + c)/3
if average >= 17 :
    print("statuse : Great")

if 12<= average < 17:
    print("status : normal")

if average < 12:
    print("statuse : fail")