import random
import string
while True:
    words=[    "apple", "ball", "cat", "dog", "egg", "fish", "go", "hat", "ice", "jump",
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
    "rat", "sun", "tap", "urn", "van", "wig", "x-ray", "yak", "zoo"]
    word=random.choice(words)
    spays=["_"]*len(word)
    shapes=["""
    +---+
    |   |
        |
        |
        |
        |""","""
    +---+
    |   |
    O   |
        |
        |
        |""","""
    +---+
    |   |
    O   |
    |   |
        |
        |""","""
    +---+
    |   |
    O   |
   /|   |
        |
        |""","""
    +---+
    |   |
    O   |
   /|\  |
        |
        |""","""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |"""]

    letter_not_count=[]
    print(" ".join(spays))
    print(shapes[0])
    counter=6
    while "_" in spays and counter !=0:
        while True:
            guess=input("enter a lettel of your guess  :\n").lower()
            if guess in string.ascii_lowercase:
                break
            else:
                print("you need to enter a letter ")
        if guess not in word and guess not in letter_not_count:
            counter-=1
            print(shapes[-counter])
            letter_not_count.append(guess)
        else:
            for x in range(len(word)):
                if word [x]==guess:
                    spays[x]=guess


        print(" ".join(spays))
        print(f"you have {counter} left")
    if "_" in spays:
        print("""you lost
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |""")
    else:
        print("""
                *** YOU WONE *** 
                """)


    repit=input("would you wanna play agine :\n").lower()
    while repit!= "yes" or repit!="no":
        print (f"we don't understand {repit} \n plise enster agean : \n")
    if repit == "yes":
        print("let start agean ")
    else:
        break