import json

# Function to save data to a JSON file
def save_data(data):     
    with open("data.json", "w") as file:             # Opens the file in write mode, which will create the file if it doesn't exist or overwrite it if it does
        json.dump(data, file)

# Function to load data from a JSON file, returns default data if file not found
def load_data():
    try:
        with open("data.json", "r") as file:         # Attempt to open the data file and load its contents
            data = json.load(file)
            
            if "users" not in data:                        # Check if the "users" key exists in the loaded data
                data["users"] = {}                         # If not, initialize it as an empty dictionary
            return data                  
                                               
    except FileNotFoundError:                        # If the file is not found, it catches the exception and returns a default data structure
        return {"users": {}}

# Load existing data or initialize new data
data = load_data()


while True:     # MAIN LOOP #


# Main loop for the login and account creation process
    while True: 
        print("\n--- WELCOME ---")
        print("1 - Login")  
        print("2 - Create account")
        print("3 - Exit")
        choose = (input("Choose an option: "))

        if choose == "1":
            username = input("Username: ")
            password = input("Password: ")
            if username in data["users"] and data["users"][username]["password"] == password:
                user = data["users"][username] 
                print(f"Welcome, {username}")
                break
            else:
                print("Invalid username or password.")

        elif choose == "2":
            username = input("Choose a username: ")
            if username in data["users"]:
                print("Username already exists.")
            else:
                password = input("Choose a password: ")
                data["users"][username] = {"password": password, "balance": 0, "history": []}
                save_data(data)                                              
                print("Account created successfully!")

        elif choose == "3":
            print("Goodbye!")
            exit()


    # Main loop for the bank system CLI, which continues until the user chooses to exit
    while True:
        print("\n--- BANK SYSTEM ---")
        print("1 - Check balance")  
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Show transaction history")
        print("5 - Exit")
        option = (input("Choose an option: "))
        
        if option == "1":
            print("Your balance is", user["balance"])

        elif option == "2":
            try:
                deposit = int(input("Insert how much you want to deposit: "))                                                  
                if deposit > 0:
                    user["balance"] += deposit                                    
                    user["history"].append(f"Deposited {deposit}")                # Appends a new entry to the transaction history list
                    save_data(data)                                               # Saves the updated data back to the JSON file
                    print("Deposit successful!")
                else:
                    print("Invalid amount.")
            except ValueError:                                                    # Handle invalid input
                print("Please enter a valid number.")
        
        elif option == "3":
            try:
                withdraw = int(input("Insert how much you want to withdraw: "))
                if withdraw <= 0:                                                 # Checks if the withdrawal amount is less than or equal to zero,
                    print("Invalid amount.")                                      # Which is invalid, and prompts the user accordingly
                elif withdraw <= user["balance"]:                                 
                    user["balance"] -= withdraw
                    user["history"].append(f"Withdrew {withdraw}")
                    save_data(data)                                               # Saves the updated data back to the JSON file
                    print("Withdraw successful!")
                    print(f"{withdraw} has been withdrawn.")
                else:                                                       
                    print("Insufficient balance.")  
            except ValueError:                                                    # Handle invalid input
                print("Please enter a valid number.")

        elif option == "4":
            if not user["history"]:                                               # If the transaction history is empty, print a message indicating it
                print("No transactions yet.")
            else:                                                                 # If there are transactions in the history, print a message indicating it
                print("Transaction History:")
                for item in user["history"]:
                    print(item)

        elif option == "5":
            print("Logging out...")
            break

        else:
            print("Please input a valid number.")