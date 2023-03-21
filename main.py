def to_encoded(password):
    password_final = []
    password = str(password)
    for x in range(len(password)):
        password_final = password_final + [encode_one(password[x])]
    password_final = ''.join(password_final)
    return password_final


def encode_one(x):
    x = int(x)
    if x in [0, 1, 2, 3, 4, 5, 6]:
        x += 3
    elif x in [7, 8, 9]:
        x -= 7
    return str(x)


def to_unencoded(password):
    password_final = []
    password = str(password)
    for x in range(len(password)):
        password_final = password_final + [unencode_one(password[x])]
    password_final = ''.join(password_final)
    return password_final

def unencode_one(x):
    x = int(x)
    if x in [3, 4, 5, 6,7, 8, 9]:
        x -= 3
    elif x in [0, 1, 2]:
        x += 7
    return str(x)


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


if name == 'main':
    loop = 1
    while loop == 1:
        menu()
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = to_encoded(password)
            print("")
        elif menu_option == 2:
            password = input("Please enter your password to encode: ")
        elif menu_option == 3:
            exit()