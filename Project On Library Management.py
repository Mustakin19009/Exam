books = ["Physics", "History", "Science", "Chemistry", "Math", "Biology"]
borrowed = []

print("📚 Library System")

while True:
    print("\n1. View Collection of Books\n2. Borrow Book\n3. Return Book\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Available Books:", books)
    elif choice == "2":
        book = input("Enter book name to borrow: ")
        if book in books:
            books.remove(book)
            borrowed.append(book)
            print(f"You borrowed '{book}'")
        else:
            print("Book not available!")
    elif choice == "3":
        book = input("Enter book name to return: ")
        if book in borrowed:
            borrowed.remove(book)
            books.append(book)
            print(f"'{book}' returned successfully.")
        else:
            print("You didn't borrow this book!")
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
