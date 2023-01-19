import random

print("Welcome to the Virtual Casino - Slot Machine Game!")

symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Sword", "Seven", "Blank"]
balance = 10

while True:
    print("You have $", balance)
    user_input = input("How much would you like to bet? \n")
    try:
        bet = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if bet > 10:
        print("You don't have enough money!")
        continue
    elif bet <= 0:
        print("Invalid input. Please enter a valid number.")
        continue

    reel_1 = random.choice(symbols)
    reel_2 = random.choice(symbols)
    reel_3 = random.choice(symbols)

    print("Spinning...")
    print("You got " + reel_1, reel_2, reel_3)
    if reel_1 == reel_2 == reel_3:
        balance = (balance + bet)
        print ("You won $", bet*2)
    else:
        balance = (balance - bet)
        print("You lost $", bet)

    if balance <= 0:
        print("Sorry, you don't have enough money to play.")
        print("Thank you for playing!")
        break

    cash_out = input("Do you want to cash out? (yes/no) \n")
    if cash_out.lower() == "yes":
        print(f"You cashed out with ${balance}")
        print("Thank you for playing!")
        break

    play_again = input("Do you want to play again? (yes/no) \n")
    if play_again.lower() == "yes":
        continue
    else:
        print("Thank you for playing!")
        break





