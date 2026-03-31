balance = 0

while True:
    print("\n--- BANK SYSTEM ---")
    print("1 - Check balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Exit")
    option = (input("Choose a option: "))
    
    if option == "1":
        print(f"Your balance is {balance}.")

    elif option == "2":
        try:
            deposit = int(input("Insert how much you want to deposit: "))
            if deposit > 0:
                balance += deposit
            else:
                print("Invalid amount.")
        except ValueError:
            print("Please enter a valid number.")
    
    elif option == "3":
        try:
            withdraw = int(input("Insert how much you want to withdraw: "))
            if withdraw <= 0:
                print("Invalid amount.")
            elif withdraw <= balance:
                balance -= withdraw
                print(f"{withdraw} has been withdrawn.")
            else:
                print("Insufficient balance.")  
        except ValueError:
            print("Please enter a valid number.")

    elif option == "4":
        print("Goodbye!")
        break

    else:
        print("Please input a valid number.")

