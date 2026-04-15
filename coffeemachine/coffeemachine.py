milk = 540
water = 400
beans = 120
cups = 9
money = 550
while True:
    Action = input("Write action (buy, fill, take, remaining, exit):\n>")
    if Action == "buy":
        coffeetype = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n>")
        if coffeetype == "1":
            if water >= 250 and beans >= 16 and cups >= 1:
                print("I have enough resources, making you a coffee!")
                water -= 250
                beans -= 16
                cups -= 1
                money += 4
            else:
                print("Sorry, not enough resources!")
        elif coffeetype == "2":
            if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
                print("I have enough resources, making you a coffee!")
                water -= 350
                milk -= 75
                beans -= 20
                cups -= 1
                money += 7
            else:
                print("Sorry, not enough resources!")
        elif coffeetype == "3":
            if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
                print("I have enough resources, making you a coffee!")
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
                money += 6
            else:
                print("Sorry, not enough resources!")
        else:
            print("Unknown coffee type")
    elif Action == "fill":
        water += int(input("Write how many ml of water you want to add:\n>"))
        milk += int(input("Write how many ml of milk you want to add:\n>"))
        beans += int(input("Write how many grams of coffee beans you want to add:\n>"))
        cups += int(input("Write how many disposable cups you want to add:\n>"))
    elif Action == "take":
        print("I gave you " + str(money))
        money = 0
    elif Action == "remaining":
        print("The coffee machine has:")
        print(str(water) + " of water")
        print(str(milk) + " of milk")
        print(str(beans) + " of coffee beans")
        print(str(cups) + " of disposable cups")
        print(str(money) + " of money")
    elif Action == "exit":
        break
