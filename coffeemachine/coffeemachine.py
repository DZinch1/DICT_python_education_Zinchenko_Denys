class coffee_machine:
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def fill(self):
        def read_int(prompt):
            while True:
                s = input(f"{prompt}\n>")
                if s.isdigit():
                    return int(s)
                print("Please enter a valid number.")

        self.water += read_int("Write how many ml of water you want to add:")
        self.milk += read_int("Write how many ml of milk you want to add:")
        self.coffee_beans += read_int("Write how many grams of coffee beans you want to add:")
        self.cups += read_int("Write how many disposable cups you want to add:")

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def take(self):
        print(f"I gave you {self.money}")
        self.money = 0

    def buy(self):
        coffeetype = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n>")
        if coffeetype == "1":
            if self.water >= 250 and self.coffee_beans >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
            else:
                if self.water < 250:
                    print("Sorry, not enough water!")
                elif self.coffee_beans < 16:
                    print("Sorry, not enough coffee beans!")
                elif self.cups < 1:
                    print("Sorry, not enough disposable cups!")
        elif coffeetype == "2":
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
            else:
                if self.water < 350:
                    print("Sorry, not enough water!")
                elif self.milk < 75:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans < 20:
                    print("Sorry, not enough coffee beans!")
                elif self.cups < 1:
                    print("Sorry, not enough disposable cups!")
        elif coffeetype == "3":
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
            else:
                if self.water < 200:
                    print("Sorry, not enough water!")
                elif self.milk < 100:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans < 12:
                    print("Sorry, not enough coffee beans!")
                elif self.cups < 1:
                    print("Sorry, not enough disposable cups!")

resources = coffee_machine(400, 540, 120, 9, 550)

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n>")
    if action == "buy":
        resources.buy()
    elif action == "fill":
        resources.fill()
    elif action == "take":
        resources.take()
    elif action == "remaining":
        resources.remaining()
    elif action == "exit":
        break
