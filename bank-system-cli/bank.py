from data_manager import save_data

def update_data(user, data):
    data["users"][user.username] = user.to_dict() 
    save_data(data)

def bank_menu(user, data):
    while True:
        print("\n--- BANK SYSTEM ---")
        print("1 - Check balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Show transaction history")
        print("5 - Logout")

        option = input("Choose an option: ").strip()

        if option == "1":
            print(f"Your balance is ${user.balance}")

        elif option == "2":
            try:
                amount = int(input("Deposit: "))
                if user.deposit(amount):
                    update_data(user, data)
                    print("Deposit successful!")
                else:
                    print("Invalid amount or insufficient balance.")
            except ValueError:
                print("Please enter a valid number.")

        elif option == "3":
            try:
                amount = int(input("Withdraw: "))
                if user.withdraw(amount):
                    update_data(user, data)
                    print("Withdraw successful!")
                else:
                    print("Invalid amount or insufficient balance.")
            except ValueError:
                print("Please enter a valid number.")

        elif option == "4":
            if not user.history:
                print("No transactions yet.")
            else:
                print("\n--- Transaction History ---")
                for item in user.history:
                    print(item)

        elif option == "5":
            print("Logging out...")
            break

        else:
            print("Please input a valid number.")