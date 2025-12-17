import random
import string
while True:
    while True:
        try:
            tell_pessword = int(input("Enter password length: "))
            break
        except:
            print("You should enter a number")

    while True:
        try:
            number_character = int(input("How many letters? "))
            break
        except:
            print("You should enter a number")

    while True:
        try:
            number_numbers = int(input("How many digits? "))
            break
        except:
            print("You should enter a number")

    while True:
        try:
            number_appearance = int(input("How many symbols? "))
            break
        except:
            print("You should enter a number")


    if number_character + number_numbers + number_appearance == tell_pessword:

        characters = random.choices(string.ascii_letters, k=number_character)
        numbers = random.choices(string.digits, k=number_numbers)
        symbols = random.choices(string.punctuation, k=number_appearance)

        # Combine all
        pess_word = characters + numbers + symbols

        # Shuffle order
        random.shuffle(pess_word)

        # Join them into ONE string
        final_password = "".join(pess_word)

        print("Your password is:", final_password)

    else:
        print("The sum doesn't equal the total length.")

    while True :
        repit=input("you wanna play agean or not :\n").lower()
        if repit=="yes" or repit == "y":
            print("here we go agean hhhhhh ")
            break
        elif repit=="no" or repit=="n":
            print("thanks for playing ")
            exit()
        else:
            print(f"please answer 'yes/y' or 'no/n' ")
