def read_from_foroshgah():
    file = open("D:\Python\foroshgah.txt")
    for line in file:
        product = line.split(",")
        product = {"id":product[0], "name":product[1], "price":product[2] , "count":product[3]}
        products.append(product)
        print(line)

def add():
    id = input(" Enter id :")
    name = input(" Enter name : ")
    price = input("Enter price : ")
    count = input("Enter count : ")
    product = {"id": id , "name": name , "price": price , "count": count}
    products.append(product)
    print(products)

def edit():
    user_choice2 = input("Enter id: ")
    user_select= input("Which one do you want to change? 1= name , 2= price , 3= count")
    for i in range(len(products)):

        if user_select == 1:
            print("Enter new name for product with code number ",products[i]["code"],": ","(current name is: ",products[i]["name"],")")
            products[i]["name"]=input()
            print("mission accomplished.")
            show_products()
            break   
        elif user_select==2:
            print("Enter new price for product with code number ",products[i]["code"],": ","(current price is: ",products[i]["price"],")")
            products[i]["price"]=input()
            print("mission accomplished.")
            show_products()
            break   
        elif user_select==3:
                print("Enter how many products with code number ",products[i]["code"]," have remained:","(remaining number is: ",products[i]["remaining"],")")
                products[i]["remaining"]=input()
                print("mission accomplished.")
                show_products()
                break
        else:
            print("wrong values")
            edit()


def delete():
    code = input("Enter the product code : ")
    for i in range(len(products)):
        if products[i]["code"] == code:
            products.remove(products[i])
            print("mission accomplished ;)")
            show_products
            break

def buy():
        for i in range (len(products)):
            code2 = input("What item do you want?  ")
            for produt in products:
                if code2 == produt["id"] or code2 == produt["name"]:
                    print(produt)
                    break
            else:
                print("not found")
            print("how many do you want؟"("products[i]"[read_from_foroshgah]))
            teedad = int(input(":"))
            if teedad <= int(products[i]["remaining"]):
                n = int(products[i]["remaining"]) - teedad
                products[i]["remaining"] = str(n)
                m = {"id":products[i]["id"],"name":products[i]["name"],"price":int(products[i]["price"])*teedad}
                shop_list ={}
                shop_list.append(m)
                print(shop_list)
                user_choice5= input("Continue shopping? yes =1 or no=2")
                if user_choice5== 1:
                    buy()
                elif user_choice5 == 2 :
                    break
                print("The product has been added to your shopping cart :)")
            else:
                print("Insufficient inventory :(")

def show_products():
    print("id \t name \t pice \t count")
    for i in range(len(products)):
        print(products[i]["id"], "\t", products[i]["name"], "\t", products[i]["pice"], "\t", products[i]["count"])

def serach():
    user_input = input("Emter keyword :")
    for produt in products:
        if user_input == produt["id"] or user_input == produt["name"]:
            print(produt)
            break
    else:
        print("not found")

def write_to_foroshgah():
    pass

def show_menu():
    print("1 - add")
    print("2 - edit")
    print("3 - delete")
    print("4 - buy")
    print("5 _ show products")
    print("6 - serach")
    print("7 _ Exit")

products = []
read_from_foroshgah()
while True:
    show_menu()
    user_choice = input("select: ")
    if user_choice == "1":
        add()
    if user_choice == "2":
        edit()
    if user_choice == "3":
        delete()
    if user_choice == "4":
        buy()
    if user_choice == "5":
        show_menu()
    if user_choice == "6":
        serach()

    if user_choice == "7" :
        write_to_foroshgah()
        exit()