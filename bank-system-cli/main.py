import json

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"balance": 0, "history": []}


data = load_data()

while True:
    print("\n--- BANK SYSTEM ---")
    print("1 - Check balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Show transaction history")
    print("5 - Exit")
    option = (input("Choose an option: "))
    
    if option == "1":
        print("Your balance is", data["balance"])

    elif option == "2":
        try:
            deposit = int(input("Insert how much you want to deposit: "))
            if deposit > 0:
                data["balance"] += deposit
                data["history"].append(f"Deposited {deposit}")
                save_data(data)
                print("Deposit successful!")
            else:
                print("Invalid amount.")
        except ValueError:
            print("Please enter a valid number.")
    
    elif option == "3":
        try:
            withdraw = int(input("Insert how much you want to withdraw: "))
            if withdraw <= 0:
                print("Invalid amount.")
            elif withdraw <= data["balance"]:
                data["balance"] -= withdraw
                data["history"].append(f"Withdrew {withdraw}")
                save_data(data)
                print("Withdraw successful!")
                print(f"{withdraw} has been withdrawn.")
            else:
                print("Insufficient balance.")  
        except ValueError:
            print("Please enter a valid number.")

    elif option == "4":
        if not data["history"]:
            print("No transactions yet.")
        else:
         for item in data["history"]:
             print(item)       

    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Please input a valid number.")

