import random
secret_number = random.randint(1, 100)

attempts = 0

while True:
    print("1 - Easy, 2 - Medium, 3 - Hard")
    dif = int(input("Choose your difficulty: "))

    if dif == 1:
        print("Easy mode selected.")
        choice = 10
        break
    elif dif == 2:
        print("Medium mode selected.")
        choice = 7
        break
    elif dif == 3:
        print("Hard mode selected.")
        choice = 5
        break
    else:
        print("Incorrect input. Please selected a difficulty: ")
        

while True:
    print(f"You have {choice} chances remaining.")
    guess = int(input("Guess a number: "))

    if guess > secret_number:
        print("Too high! Try again")
        choice -= 1
        
    elif guess < secret_number:
        print("Too low! Try again")
        choice -= 1
            
    else:
        print(f"Congratulations! You guessed the number {secret_number}")
        break

    if choice == 0:
        print(f"You lost! The number is {secret_number}")
        break