from data_manager import load_data
from auth import login, create_account
from bank import bank_menu

data = load_data()

while True:
    print("\n--- WELCOME ---")
    print("1 - Login")
    print("2 - Create account")
    print("3 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        user = login(data)

        if user:
            bank_menu(user, data)

    elif choice == "2":
        create_account(data)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Please input a valid number.")