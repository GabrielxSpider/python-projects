import json

# Function to save data to a JSON file
def save_data(data):     
    with open("data.json", "w") as file:             
        json.dump(data, file)

# Function to load data from a JSON file, returns default data if file not found
def load_data():
    try:
        with open("data.json", "r") as file:         
            data = json.load(file)
            
            if "users" not in data:                        
                data["users"] = {}                         
            return data                  
                                               
    except FileNotFoundError:                        
        return {"users": {}}