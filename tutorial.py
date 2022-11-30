import random


def computer_input():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    return computer_choice

def user_input():
    options = ["rock", "paper", "scissors"]
    user_choice = input("1:rock\n2:paper\n3:scissors\n")

    if user_choice == "1":
        return options[0]

    elif user_choice == "2":
        return options[1]

    elif user_choice == "3":
        return options[2]

    else:
        print("You Didn't Enter Any Of The Numbers!")

def result():
    x = computer_input()
    y = user_input()

    if x == y:
        print(x, " - ", y, "\nTie!")

    elif x == "rock" and y == "paper":
        print(x, " - ", y, "\nYou Won!")

    elif x == "rock" and y == "scissors":
        print(x, " - ", y, "\nYou Lost!")

    elif x == "paper" and y == "rock":
        print(x, " - ", y, "\nYou Lost!")

    elif x == "paper" and y == "scissors":
        print(x, " - ", y, "\nYou Won!")

    elif x == "scissors" and y == "rock":
        print(x, " - ", y, "\nYou Won!")

    elif x == "scissors" and y == "paper":
        print(x, " - ", y, "\nYou Lost!")

    else:
        exit()

result()