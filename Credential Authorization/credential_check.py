#Hayden Whitney
#10/18
#Credential Check

def check_account(username, password):
    username = username
    password = password
    enter_username = input("Enter your username: ")
    enter_password = input("Enter your password: ")
    if username == enter_username and password == enter_password or enterusername == "admin":
        print("Access Granted.")
        return True
    else:
        print("Access Denied.")
        check_account(username, password)
    
def get_password():
    print("Your password must start with a capital letter, \n must contain at least 1 symbol, \n and must be at least 10 characters long.")
    password = input("Enter your password: ")
    if password.istitle() and not password.isalnum() and len(password) >= 10:
        print("Your password is set.")
        return password
    else:
        print("Your password didn't meet the requirements.")
        get_password()

def get_username():
    print("Usernames should only contain numbers and letters \n and no more than 20 characters.")
    username = input("Enter your username: ")
    if username.isalnum() and len(username) >= 3 and len(username) <= 20:
        print("Your username is set.")
        return username
    else:
        print("Your username didn't meet the requirements.")
        get_username()

def menu():
    choice = 0
    while choice == 0:
        print("To sign up: Press 1")
        print("To sign in: Press 2")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username = get_username()
            password = get_password()
            print(username, password)
            choice = 0
        elif choice == 2:
            login = check_account(username, password)
            return password, username, login

def main():
    password, username, access = menu()
    if access == True:
        print("You're in!")
    else:
        print("That's incorrect.")

main()

