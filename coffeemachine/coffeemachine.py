milk = 540
water = 400
beans = 120
cups = 9
money = 550
print(f"""The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{money} of money""")

Action = input("Write action (buy, fill, take):\n>")
if Action == "buy":
        coffeetype = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n>")
        if coffeetype == "1":
            if water >= 250 and beans >= 16 and cups >= 1:
                water -= 250
                beans -= 16
                cups -= 1
                money += 4
                print(f"The coffee machine has:")
                print(f"{water} of water")
                print(f"{milk} of milk")
                print(f"{beans} of coffee beans")
                print(f"{cups} of disposable cups")
                print(f"{money} of money")

            else:
                print("Sorry, not enough resources!")
        elif coffeetype == "2":
            if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
                water -= 350
                milk -= 75
                beans -= 20
                cups -= 1
                money += 7
                print(f"The coffee machine has:")
                print(f"{water} of water")
                print(f"{milk} of milk")
                print(f"{beans} of coffee beans")
                print(f"{cups} of disposable cups")
                print(f"{money} of money")
            else:
                print("Sorry, not enough resources!")
        elif coffeetype == "3":
            if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
                money += 6
                print(f"The coffee machine has:")
                print(f"{water} of water")
                print(f"{milk} of milk")
                print(f"{beans} of coffee beans")
                print(f"{cups} of disposable cups")
                print(f"{money} of money")
            else:
                print("Sorry, not enough resources!")
        else:
            print("Unknown coffee type")
elif Action == "fill":
    water += int(input("Write how many ml of water you want to add:\n>"))
    milk += int(input("Write how many ml of milk you want to add:\n>"))
    beans += int(input("Write how many grams of coffee beans you want to add:\n>"))
    cups += int(input("Write how many disposable cups you want to add:\n>"))
    print(f"The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")
elif Action == "take":
    print("I gave you " + str(money))
    money = 0
    print(f"The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")
