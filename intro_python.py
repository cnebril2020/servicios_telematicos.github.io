ent = 5
string = "Carlos"
list = ["Carlos", "Alejandra", "María", "Davicho", "David"]
dict = {list[0]: 654631207, list[1]: 664108913, list[2]: 664108913, list[3]: 629814241, list[4]: 678657463}
list2 = []

print(dict)
print("hola buenos dias")


def multiplication_tables():
    count = 1
    exit = False
    msg = ""
    while not exit:
        msg += "TABLA DEL " + str(count) + "\n"
        for i in range(11):
            var = count * i
            msg += str(count) + " * " + str(i) + " es igual a " + str(var) + "\n"
            var += 1
        count += 1
        msg += "----------------------" + "\n"
        if count == 11:
            exit = True

    return msg


def one_table(num):
    for i in range(11):
        print(str(num) + " * " + str(i) + " = " + str(i * num))

def multiplication_tablesv2():
    for i in range(11):
        one_table(i)


def tower():
    try:
        user_num = int(input("Please write a number: "))
        for i in range(user_num):
            for j in range(i + 1):
                print("*", end="")
            print()
    except:
        print("Please, we need a NUMBER.")




def menu():
    msg = ""
    msg += "1.- Insertar\n"
    msg += "2.- Mostrar\n"
    msg += "3.- Salir\n"

    return msg

def insert_list(buy_list, dict):
    user_fruit = input("What fuit do you want to add? ")
    if user_fruit in dict.keys():
        print("fruit added")
        buy_list.append(user_fruit)
    else:
        print("There is no such thing in the supermarket.")

def view_list(dict):
    print(dict.keys())



dict = {"manzana": 7, "naranjas": 4, "uvas": 4, "melón": 32, "sandia": 2}
buy_list = []
exit = False
while not exit:
    print(menu())
    o = int(input("Please select an option: "))
    if o == 1:
        insert_list(buy_list, dict)
    elif o == 2:
        view_list(dict)
    else:
        exit = True