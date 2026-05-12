import random
import time

operators = ["+", "-", "*"]
DESCRIPTIONS = {
    1: "simple operations with numbers 2-9",
    2: "integral squares of 11-29",
    3: "arithmetic expressions with 3 numbers",
}

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Incorrect format.")

def ask_yes_no(prompt: str) -> bool:
    answer = input(prompt).strip().lower()
    return answer in ("yes", "y")

def save_result(name: str, score: int, level: int, duration: float,) -> None:
    desc = DESCRIPTIONS.get(level, "")
    line = f"{name}: {score}/5 in level {level} ({desc}) Time: {duration:.2f} seconds\n"
    try:
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(line)
    except OSError as e:
        print(f"Failed to save result: {e}")

def _apply_op(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b

def evaluate_three(a, op1, b, op2, c):
    if op1 == "*" and op2 != "*":
        return _apply_op(_apply_op(a, op1, b), op2, c)
    if op2 == "*" and op1 != "*":
        return _apply_op(a, op1, _apply_op(b, op2, c))
    return _apply_op(_apply_op(a, op1, b), op2, c)

def level_simple_questions(count: int = 5):
    correct = 0
    start = time.perf_counter()
    for i in range(count):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(operators)
        print(f"{a} {op} {b}")
        answer = read_int(">")
        expected = _apply_op(a, op, b)
        if answer == expected:
            print("Right!")
            correct += 1
        else:
            print("Wrong!")
    duration = time.perf_counter() - start
    print(f"Your mark is {correct}/{count}.")
    return correct, duration


def level_squares(count: int = 5):
    correct = 0
    start = time.perf_counter()
    for i in range(count):
        a = random.randint(11, 29)
        print(f"{a}")
        answer = read_int(">")
        if answer == a * a:
            print("Right!")
            correct += 1
        else:
            print("Wrong!")
    duration = time.perf_counter() - start
    print(f"Your mark is {correct}/{count}.")
    return correct, duration


def level_three_terms(count: int = 5):
    correct = 0
    start = time.perf_counter()
    for i in range(count):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        op1 = random.choice(operators)
        op2 = random.choice(operators)
        print(f"{a} {op1} {b} {op2} {c}")
        answer = read_int(">")
        expected = evaluate_three(a, op1, b, op2, c)
        if answer == expected:
            print("Right!")
            correct += 1
        else:
            print("Wrong!")
    duration = time.perf_counter() - start
    print(f"Your mark is {correct}/{count}.")
    return correct, duration

LEVEL_FUNCS = {
    1: level_simple_questions,
    2: level_squares,
    3: level_three_terms,
}


def main():
       while True:
            level = read_int("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n3 - arithmetic expressions with 3 numbers\n>")
            if level not in LEVEL_FUNCS:
                print("Invalid level. Please enter 1, 2, or 3.")
                continue
            func = LEVEL_FUNCS[level]
            score, duration = func()
            if ask_yes_no("Would you like to save your result to the file? Enter yes or no.\n>"):
                name = input("Enter your name:\n>")
                save_result(name, score, level, duration)
            if not ask_yes_no("Do you want to try another level? Enter yes or no.\n>"):
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()
