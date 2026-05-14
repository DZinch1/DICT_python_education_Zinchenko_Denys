import random

Options = {}

Commands = ["!exit", "!rating", "!options"]

def select_options():
    user_input = input("Enter the options you want to play with:\n>").lower()
    if user_input.strip() == "":
        return ["rock", "paper", "scissors"]
    selected_options = [option.strip() for option in user_input.split(",")]
    if len(selected_options) < 3:
        print("At least 3 options are required.")
        return select_options()
    return selected_options


def get_user_choice():
    while True:
        user_input = input("Enter your choice:\n>").lower()
        if user_input in Options or user_input in Commands:
            return user_input
        else:
            print("Invalid input.")


def get_computer_choice():
    return random.choice(Options)


def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    user_idx = Options.index(user_choice)
    n = len(Options)
    beaten = [(user_idx - i) % n for i in range(1, n // 2 + 1)]
    if Options.index(computer_choice) in beaten:
        return "win"
    else:
        return "lose"


def rating():
    ratings = {}
    try:
        with open("rating.txt", "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) != 2:
                    continue
                name, score = parts
                try:
                    ratings[name] = int(score)
                except ValueError:
                    continue
    except FileNotFoundError:
        open("rating.txt", "w").close()
    return ratings


def update_rating(name, score):
    ratings = rating()
    ratings[name] = score
    with open("rating.txt", "w") as file:
        for n, s in ratings.items():
            file.write(f"{n} {s}\n")


def input_name():
    name = input("Enter your name:\n>")
    print(f"Hello, {name}!")
    return name


def main():
    name = input_name()
    global Options
    Options = select_options()
    ratings = rating()
    score = ratings.get(name, 0)
    print("Okay, let`s start")
    while True:
        user_choice = get_user_choice()
        if user_choice == "!exit":
            update_rating(name, score)
            print("Bye!")
            break
        elif user_choice == "!rating":
            print(f"Your rating: {score}")
            continue
        elif user_choice == "!options":
            print (f"Current options: {', '.join(Options)}")
            continue
        computer_choice = get_computer_choice()
        result = winner(user_choice, computer_choice)
        if result == "win":
            print (f"Well done. Computer chose {computer_choice} and failed")
            score += 100
        elif result == "draw":
            print (f"There is a draw ({computer_choice})")
            score += 50
        else:
            print (f"Sorry, but computer chose {computer_choice}")


if __name__ == "__main__":
    main()
