def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

formatters = [
    "plain", "bold", "italic", "header", "link",
    "inline-code", "ordered-list", "unordered-list", "new-line"
]

def help():
    print("Available formatters: " + ", ".join(formatters))
    print("Special commands: !help, !done")

output_text = ""

def output(s):
    global output_text
    output_text += s

def main():
    global output_text
    while True:
        user_input = input("Choose a formatter: >")
        if user_input == "!help":
            help()
        elif user_input == "!done":
            with open("output.md", "w", encoding="utf-8") as f:
                f.write(output_text)
            break
        elif user_input in formatters:
            if user_input == "plain":
                text = input("Text: >")
                formatted = text
                output(formatted)
            elif user_input == "bold":
                text = input("Text: >")
                formatted = f"**{text}**"
                output(formatted)
            elif user_input == "italic":
                text = input("Text: >")
                formatted = f"*{text}*"
                output(formatted)
            elif user_input == "header":
                while True:
                    level = read_int("Level: >")
                    if 1 <= level <= 6:
                        text = input("Text: >")
                        formatted = f"\n\n{'#' * level} {text}\n\n"
                        output(formatted)
                        break
                    else:
                        print("The level should be within the range of 1 to 6")
            elif user_input == "link":
                label = input("Label: >")
                url = input("URL: >")
                formatted = f"[{label}]({url})"
                output(formatted)
            elif user_input == "inline-code":
                text = input("Text: >")
                formatted = f"`{text}`"
                output(formatted)
            elif user_input in ["ordered-list", "unordered-list"]:
                rows = read_int("Number of rows: >")
                if rows <= 0:
                    print("The number of rows should be greater than zero")
                    continue
                lines = ["\n\n"]
                for i in range(1, rows + 1):
                    row_text = input(f"Row #{i}: >")
                    if user_input == "ordered-list":
                        lines.append(f"{i}. {row_text}\n")
                    else:
                        lines.append(f"* {row_text}\n")
                lines.append("\n")
                formatted = "".join(lines)
                output(formatted)
            elif user_input == "new-line":
                output("\n\n")
        else:
            print("Unknown formatting type or command")
            continue

if __name__ == "__main__":
    main()
