while True:
    prices = []
    things = []

    print("Hello, this is your basket 🧺")
    while True:
        try:
            number_basket = int(input("How many items do you have in your basket? \n "))
            break
        except:
            print("you need to enter a number 1 or more than it ")
    while True:
        if number_basket==0 or number_basket <0:
            print("you need to enter a number 1 or more than it ")
        else:
            print()
        break

    for i in range(1, number_basket + 1):
        print(f"\nItem {i}:")
        thing = input("Please tell me the name of the item: \n ")
        things.append(thing)

        price = int(input("How much is it? \n "))
        prices.append(price)

    # Show items
    choice = input("\nDo you want to see what you have in your basket? (yes/no): \n ").lower()
    if choice == "yes":
        print(f"🛒 Your items: {things}")
    elif choice == "no":
        print("Okay, skipping.")
    else:
        print(f"⚠️ We don't understand '{choice}'.")

    # Show prices
    choice2 = input("\nDo you want to see the prices? (yes/no): \n ").lower()
    if choice2 == "yes":
        print(f"💲 Prices:{prices}")
        total = sum(prices)   
        print(f"💰 Total = {total}")
    elif choice2 == "no":
        print("Okay, skipping.")
    else:
        print(f"⚠️ We don't understand '{choice2}'.")
