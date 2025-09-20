import random
while True:
    # ASCII art
    siser = """...scissors art..."""
    rock = """...rock art..."""
    paper = """...paper art..."""

    print("Welcome to our game!")
    print("We will play Rock, Paper, Scissors 🎮")

    # Player choice
    chose = input("Enter your choice ('rock', 'paper', or 'siser'): \n").lower()

    if chose == "rock":
        print(rock)
    elif chose == "paper":
        print(paper)
    elif chose == "siser":
        print(siser)
    else:
        print("⚠️ You need to choose correctly (rock/paper/siser)")

    # Computer choice
    computor_chose = random.choice(["rock", "paper", "siser"])
    print("\nComputer chose:")
    if computor_chose == "rock":
        print(rock)
    elif computor_chose == "paper":
        print(paper)
    elif computor_chose == "siser":
        print(siser)

    # Decide winner
    print("\n--- Result ---")
    if chose == computor_chose:
        print("🤝 It's a tie!")
    elif (chose == "rock" and computor_chose == "siser") or \
        (chose == "paper" and computor_chose == "rock") or \
        (chose == "siser" and computor_chose == "paper"):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

