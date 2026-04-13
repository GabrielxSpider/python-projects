from data_manager import load_data
from auth import login, create_account
from bank import bank_menu

class BankSystem:
    def __init__(self):
        self.data = load_data()

    def run(self):
        while True:
            print("\n--- WELCOME ---")
            print("1 - Login")
            print("2 - Create account")
            print("3 - Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                user = login(self.data)

                if user:
                    bank_menu(user, self.data)

            elif choice == "2":
                create_account(self.data)

            elif choice == "3":
                print("Goodbye!")
                break

            else:
                print("Please input a valid number.")