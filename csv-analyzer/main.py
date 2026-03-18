import csv

# List to store numeric values from the CSV file
values = []

# Open and read the CSV file
with open("data.csv", newline="") as file:
    reader = csv.reader(file)

    # Iterate through each row in the file
    for row in reader:
        try:
            number = float(row[0])  # Convert value to float
            values.append(number)   # Add valid number to the list
        except:
            pass  # Ignore invalid data

# Check if there are valid values
if len(values) > 0:
    total = len(values)
    total_sum = sum(values)
    average = total_sum / total
    maximum = max(values)
    minimum = min(values)

    # Display results
    print("Total values:", total)
    print("Average:", average)
    print("Maximum value:", maximum)
    print("Minimum value:", minimum)
else:
    print("No valid data found.")