books=[]

loproli=input("enter name of a book you have : \n").lower()
books.append(loproli)

loproli2=input("enter name of a nother book you have or prees enter if you wane skep : \n").lower()
if loproli2!="":
    books.append(loproli2)
    print(f"your labroli is {books}")
else:
    print(f"you labre is {books}")


wish_books=[]

wish1=input("enter name of book you wish you have to : \n ").lower()
wish_books.append(wish1)

wish2=input("so give anothe book or prees enter to skip :\n").lower()
if wish2!="":
    wish_books.append(wish2)
    print(f"you wish you have {wish_books} and you have {books}")
else:
    print(f"you wish you have {wish_books} and you have {books}")



move=input("what the book you oradi have in list of wish books or press enter to skip :  \n").lower()
if move!="":
    print(f"nawe you lise is \n you laproli {books} \n your list in wish books is {wish_books}")
    if move==wish_books[0]:
      books.append(wish_books [0])
      wish_books.remove(wish_books[0])
    elif move==wish_books[1]:
       books.append(wish_books[1])
       wish_books.remove(wish_books[1])
    else:
        print(f"you do't have {move} in you lise of wish books ")
print(f"nawe you lise is \n you laproli {books} \n your list in wish books is {wish_books}")

remove=input("what the book you wanna you sail it or press enter to skip : \n ").lower()
if remove!="":
    if remove==books[0]:
      books.remove(books[0])
    elif remove==books[1]:
        books.remove(books[1])
    elif remove==books[2]:
        books.remove(books[2])
        print(f"you labrela is {books}")
print(f"you labrela is {books}")