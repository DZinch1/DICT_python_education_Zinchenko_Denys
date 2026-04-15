waterforcup = 200
milkforcup = 50
beansforcup = 15

water = int(input("Write how many ml of water coffee machine has?\n>"))
milk = int(input("Write how many ml of milk coffee machine has?\n>"))
beans = int(input("Write how many grams of coffee beans coffee machine has?\n>"))
cups = int(input("Write how many cups yiu will need?\n>"))

possiblecupswater = water // waterforcup
possiblecupsmilk = milk // milkforcup
possiblecupsbeans = beans // beansforcup

if possiblecupswater <= possiblecupsmilk and possiblecupswater <= possiblecupsbeans:
    possiblecups = possiblecupswater
elif possiblecupsmilk <= possiblecupswater and possiblecupsmilk <= possiblecupsbeans:
    possiblecups = possiblecupsmilk
else:
    possiblecups = possiblecupsbeans


if possiblecups == cups:
    print("Yes, I can make that amount of coffee")
elif possiblecups > cups:
    print("Yes, I can make that amount of coffee (and even " + str(possiblecups - cups) + " more than that)")
else:
    print("No, I can make only " + str(possiblecups) + " cups of coffee")
