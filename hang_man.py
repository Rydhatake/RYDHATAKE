import random
import string

while True:
    words = [
        "apple", "ball", "cat", "dog", "egg", "fish", "go", "hat", "ice", "jump",
        "kite", "lion", "man", "nose", "open", "pen", "queen", "run", "sun", "tree",
        "up", "van", "water", "x-ray", "yes", "zebra", "air", "bed", "car", "day",
        "ear", "fun", "girl", "hand", "ink", "job", "key", "leg", "moon", "net",
        "owl", "pig", "quit", "rat", "star", "top", "use", "vet", "win", "box",
        "yarn", "zero", "ant", "bag", "cup", "door", "eye", "fan", "girl", "hat",
        "iron", "jam", "kid", "log", "map", "nap", "oil", "pot", "queen", "rope",
        "sit", "toy", "urn", "van", "web", "yak", "zip", "arm", "boy", "cap",
        "desk", "ear", "fog", "goat", "hill", "ice", "jar", "kite", "leaf", "man",
        "net", "ox", "pen", "quilt", "run", "sun", "top", "up", "vase", "wig",
        "xylophone", "yarn", "zoo", "bat", "cow", "dig", "ear", "fan", "gas",
        "hat", "ink", "jet", "key", "lip", "mud", "nap", "oak", "pig", "rat",
        "sap", "tap", "urn", "vet", "wax", "yak", "zip", "ant", "bag", "cap",
        "dot", "egg", "fig", "gun", "hen", "ink", "jar", "kit", "log", "mat",
        "net", "owl", "pen", "ram", "sun", "tap", "urn", "van", "wig", "box",
        "yak", "zip", "air", "bat", "cat", "dog", "egg", "fox", "go", "hen",
        "ice", "jam", "kid", "lap", "man", "net", "oak", "pig", "quill", "rat",
        "sun", "tap", "urn", "van", "web", "x-ray", "yak", "zoo", "ape", "bug",
        "cow", "dig", "elf", "fig", "gum", "hat", "ink", "jug", "kit", "lid",
        "mud", "nut", "owl", "pan", "quip", "ram", "sip", "tap", "urn", "vet",
        "wax", "yak", "zip", "art", "bat", "cat", "dot", "egg", "fox", "gut",
        "hat", "ice", "jet", "kit", "lip", "man", "net", "oak", "pig", "quill",
        "rat", "sun", "tap", "urn", "van", "wig", "x-ray", "yak", "zoo"
    ]

    word = random.choice(words)
    spays = ["_"] * len(word)
    shapes = [
        """
        +---+
        |   |
            |
            |
            |
            |""",
        """
        +---+
        |   |
        O   |
            |
            |
            |""",
        """
        +---+
        |   |
        O   |
        |   |
            |
            |""",
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |""",
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |""",
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |""",
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |"""
    ]

    letter_not_count = []
    counter = 6
    print(" ".join(spays))
    print(shapes[0])

    while "_" in spays and counter > 0:
        while True:
            guess = input("Enter a letter: ").lower()
            if guess in string.ascii_lowercase and len(guess) == 1:
                break
            else:
                print("You need to enter a single letter.")

        if guess not in word and guess not in letter_not_count:
            counter -= 1
            letter_not_count.append(guess)
        else:
            for i, ch in enumerate(word):
                if ch == guess:
                    spays[i] = guess

        print(" ".join(spays))
        print(shapes[6 - counter])
        print(f"You have {counter} guesses left.")

    if "_" in spays:
        print("You lost!")
        print(shapes[-1])
        print(f"The word was: {word}")
    else:
        print("*** YOU WON! ***")

    while True:
        repit = input("Do you want to play again? (yes/no): ").lower()
        if repit in ["yes", "no"]:
            break
        print(f"We don't understand '{repit}', please enter again.")

    if repit == "no":
        break
