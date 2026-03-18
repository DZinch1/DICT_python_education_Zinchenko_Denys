import random

print("How many pencils would you like to use:")
while True:
    pencils_str = input('>')
    if not pencils_str.isdigit():
        print("The number of pencils should be numeric")
        continue
    pencils = int(pencils_str)
    if pencils == 0:
        print("The number of pencils should be positive")
        continue
    break

name1, name2 = "John", "Jack"  # John - людина, Jack - бот
print(f"Who will be the first ({name1}, {name2}):")
while True:
    current_player = input('>')
    if current_player not in [name1, name2]:
        print(f"Choose between {name1} and {name2}")
        continue
    break

next_player = name2 if current_player == name1 else name1

while pencils > 0:
    print("|" * pencils)
    print(f"{current_player}'s turn!")

    if current_player == name2:
        if pencils == 1:
            taken = 1
        elif pencils % 4 == 0:
            taken = 3
        elif pencils % 4 == 3:
            taken = 2
        elif pencils % 4 == 2:
            taken = 1
        else:
            taken = random.randint(1, 3)

        print(taken)

    else:
        while True:
            taken_str = input('>')
            if taken_str not in ['1', '2', '3']:
                print("Possible values: '1', '2' or '3'")
                continue
            taken = int(taken_str)
            if taken > pencils:
                print("Too many pencils were taken")
                continue
            break

    pencils -= taken

    if pencils == 0:
        print(f"{next_player} won!")
        break

    current_player, next_player = next_player, current_player