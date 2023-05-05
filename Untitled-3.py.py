import math
while True :
    x = input("do you want to start? (yes/no): ")
    if x == "yes" :
    
        num1 = int(float(input("Enter num1 : ")))
        num2 = int(float(input("Enter num2 : ")))

        op = input("Specify your operation type.you can chosse(+ , - , / , * , radical , sin , cos , tan , cot , factorial) : ")
        if op == "+" :
            result = num1  + num2
        if op == "-" :
            result = num1 - num2
        if op == "/" :
            if num2 ==0 :
                result = "Erorr"
            else:
             result = num1 / num2    
        if op == "*" :
            result = num1 * num2
        if op == "tan" :
            a = input("num1 or num2 ? : ")
        if a == "num1" :
           result = math.tan(num1)
        if a == "num2":
            result = math.tan(num2) 
        if op == "radical":
            a = input("num1 or num2 ? : ")
        if a == "num1":
            result= math.radical(num1)
        if a == "num2":
            result= math.radical(num2)
        if op == "sin":
            a = input("num1 or num2 ? :")
        if a == "num1":
            result= math.sin(num1)
        if a == "num2:":
            result = math.sin(num2)
        if op == "cos":
            a = input("num1 or num2 ? :")
        if a == "num1":
            result = math.cos(num1)
        if a == "num2":
            result= math.cos(num2)
        if op == "cot":
            a = input("num1 or num2 ? :")
        if a == "num1":
            result = math.cot(num1)
        if a =="num2":
            result = math.cot(num2)
        if op == "factorial":
            a = input("num1 or num2 ? :")
        if a == "num1":
            result = math.floor(num1)
        if a =="num2":
            result = math.floor(num2)
        print("result : " , result)
    else:
        break
