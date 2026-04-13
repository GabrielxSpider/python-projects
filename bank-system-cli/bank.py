from data_manager import save_data

def bank_menu(user, data):
    while True:
        print("\n--- BANK SYSTEM ---")
        print("1 - Check balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - TransactionHistory")
        print("5 - Logout")

        option = input("Choose: ")

        if option == "1":
            print(user["balance"])

        elif option == "2":
            deposit = int(input("Deposit: "))
            if deposit > 0:
                user["balance"] += deposit
                user["history"].append(f"Deposited {deposit}")
                save_data(data)

        elif option == "3":
            withdraw = int(input("Withdraw: "))
            if 0 < withdraw <= user["balance"]:
                user["balance"] -= withdraw
                user["history"].append(f"Withdrew {withdraw}")
                save_data(data)

        elif option == "4":
            for item in user["history"]:
                print(item)

        elif option == "5":
            break