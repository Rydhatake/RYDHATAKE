import random

while True:
    number = random.randint(1, 50)
    print("Welcome to our game!\nGuess the number between 1 and 50.")

    attempts = 0

    while True:
        try:
            guess = int(input("Enter your number: "))
        except ValueError:
            print("Enter a valid integer.")
            continue

        if 1 <= guess <= 50:
            attempts += 1

            if guess > number:
                print(f"Wrong! The right number is lower than {guess}.")
            elif guess < number:
                print(f"Wrong! The right number is higher than {guess}.")
            else:
                print(f"Correct! The number was {number}.")
                print(f"You guessed it in {attempts} attempts.")

                if attempts == 1:
                    print("You're insanely lucky!")
                elif attempts <= 4:
                    print("You're a master!")
                elif attempts <= 10:
                    print("Not bad, but not impressive either.")
                else:
                    print("Bro… you need some training 😭")
                break
        else:
            print("Number must be between 1 and 50.")
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