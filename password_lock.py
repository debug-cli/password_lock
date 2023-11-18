
def set_password():
    password = input("Enter your new password: ")
    with open("password.txt", "w") as file:
        file.write(password)
    return password

def get_saved_password():
    try:
        with open("password.txt", "r") as file:
            saved_password = file.read().strip()
            return saved_password
    except FileNotFoundError:
        return None

def unlock(saved_password):
    password_attempt = input("Enter the password: ")
    if password_attempt == saved_password:
        print("Password correct. Access granted!")
        # Add your code here to do something once the password is correct
    else:
        print("Incorrect password. Access denied.")

def main():
    print("Welcome to the Interstellar Lock")
    saved_password = get_saved_password()
    while True:
        choice = input("Enter 'S' to set a new password or 'U' to unlock: ").upper()
        if choice == 'S':
            saved_password = set_password()
            print("Password set successfully!")
            break
        elif choice == 'U':
            if saved_password:
                unlock(saved_password)
                break
            else:
                print("Password not set. Please set a password first.")
        else:
            print("Invalid choice. Please enter 'S' or 'U'.")

if __name__ == "__main__":
    main()
