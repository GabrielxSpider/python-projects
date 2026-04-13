from utils import hash_password
from data_manager import save_data

def login(data):
    username = input("Username: ")
    password = input("Password: ")

    if username in data["users"]:
        user = data["users"][username]

        if user["password"] == hash_password(password):
            print(f"Welcome, {username}")
            return user

    print("Invalid username or password.")
    return None


def create_account(data):
    username = input("Choose a username: ")

    if username in data["users"]:
        print("Username already exists.")
        return

    password = input("Choose a password: ")

    data["users"][username] = {
        "password": hash_password(password),
        "balance": 0,
        "history": []
    }

    save_data(data)
    print("Account created!")