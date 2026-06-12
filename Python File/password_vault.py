# password_vault.py

def add_record():

    website = input("Enter Website Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open("password_vault.txt", "a") as file:

        file.write(f"Website : {website}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write("-" * 30 + "\n")

    print("\nRecord Saved Successfully!")


def display_records():

    print("\n===== SAVED RECORDS =====\n")

    try:
        with open("password_vault.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("No records found.")


while True:

    print("\n===== PASSWORD VAULT =====")
    print("1. Add Record")
    print("2. Display Records")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_record()

    elif choice == "2":
        display_records()

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
