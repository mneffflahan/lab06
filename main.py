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

def decode(encoded_password):
    encoded_list = list(encoded_password)
    for x in range(len(encoded_list)):
        if encoded_list[x] == "0":
            encoded_list[x] = "7"
        elif encoded_list[x] == "1":
            encoded_list[x] = "8"
        elif encoded_list[x] == "2":
            encoded_list = "9"
        else:
            encoded_list[x] = int(encoded_list[x])
            encoded_list[x] = int(encoded_list[x] - 3)
            encoded_list[x] = str(encoded_list[x])
    password = ''.join(encoded_list)
    return password


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


if __name__ == '__main__':
    loop = 1
    while loop == 1:
        menu()
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = to_encoded(password)
            print("Your password has been encoded and stored!")
        elif menu_option == 2:
            print("The encoded password is", encoded_password, "and the original password is", password)
        elif menu_option == 3:
            exit()
