books = []

# Add first book
loproli = input("Enter name of a book you have: \n").lower()
if loproli:
    books.append(loproli)

# Add second book (optional)
loproli2 = input("Enter another book you have (or press Enter to skip): \n").lower()
if loproli2:
    books.append(loproli2)

print(f"Your library: {books}")

# Wishlist
wish_books = []

wish1 = input("Enter name of a book you wish to have: \n").lower()
if wish1:
    wish_books.append(wish1)

wish2 = input("Enter another wish book (or press Enter to skip): \n").lower()
if wish2:
    wish_books.append(wish2)

print(f"You wish for: {wish_books}")
print(f"You already have: {books}")

# Move a book from wish list to library
move = input("Enter a book you already got from your wish list (or press Enter to skip): \n").lower()
if move in wish_books:
    wish_books.remove(move)
    books.append(move)
    print(f"✅ Moved '{move}' from wish list to library.")
else:
    if move:
        print(f"⚠️ '{move}' is not in your wish list.")

print(f"Your library: {books}")
print(f"Your wish list: {wish_books}")

# Remove (sell) a book
remove = input("Enter the book you want to sell (or press Enter to skip): \n").lower()
if remove in books:
    books.remove(remove)
    print(f"✅ You sold '{remove}'.")
else:
    if remove:
        print(f"⚠️ '{remove}' is not in your library.")

print(f"📚 Final library: {books}")
