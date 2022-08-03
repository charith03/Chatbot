string = input("Enter a string: ")

print("1. convert the input string into upper case.")

print("2. convert the input string into lower case.")

print("3. Check whether all the character of the input string are in upper case.")

print("4. Check whether all the character of the input string are in lower case.")

print("5. Replace the string 'INTELLIgence' by 'Neural Network'.")

print("6. Check whether the given string starts with 'T'.")

print("7. Check whether the given string ends with 'e'.")

print("8. Convert the first letter of the input string into capital letter.")

print("9. Convert the lower-case characters to upper case and vice versa.")

print("10. Exit")

print("-" * 20)


def switch(string, option):
    match option:

        case 1:

            print(string.upper())

        case 2:

            print(string.lower())

        case 3:

            print(string.isupper())

        case 4:

            print(string.islower())

        case 5:

            print(string.replace("INTELLIgence", "Neural Network"))

        case 6:

            print(string.startswith("T"))

        case 7:

            print(string.endswith("e"))

        case 8:

            print(string.capitalize())

        case 9:

            print(string.swapcase())


while True:

    option = int(input("Choose any option: "))

    if option == 10:
        print("...Program Terminated...")

        break

        switch(string, option)