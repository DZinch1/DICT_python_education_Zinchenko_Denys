print("Hello! My name is DICT_Bot.")
print("I was created in 2025.")
name  = input("Please, remind me your name:\n" )
print("What a great name you have", name, "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is:", age, "; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
for i in range(number+1):
    print(i, "!")
print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print("What does the len() function return when passed a string?\n"
      "1. Always the number 1\n"
      "2. The code of the first character in the string\n"
      "3. The number of characters in the string\n"
      "4. An error, because len() don`t works with string")
while True:
    num = int(input())
    if num == 3:
        print("Completed, have a nice day!")
        break
    else:
        print("Please try again.")
print("Congratulations, have a nice day!")