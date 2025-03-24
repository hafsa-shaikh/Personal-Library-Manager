import os
import json

library = []  # Library list

FILE_NAME = "library_data.txt"

# Load data from file
def load_library():
    global library
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            try:
                library = json.load(file)
            except json.JSONDecodeError:
                library = []

# Save data to file
def save_library():
    with open(FILE_NAME, 'w') as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print("✅ Book added successfully!")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("🗑️ Book removed successfully!")
            return
    print("⚠️ Book not found.")

# Search books
def search_books():
    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book in library:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            display_book(book)
            found = True
    if not found:
        print("🔍 No matching books found.")

# Display a single book
def display_book(book):
    status = "Read" if book["read"] else "Unread"
    print(f"📖 {book['title']} by {book['author']} ({book['year']}), Genre: {book['genre']}, Status: {status}")

# Display all books
def display_all_books():
    if not library:
        print("📚 Library is empty.")
    else:
        for book in library:
            display_book(book)

# Display statistics
def display_statistics():
    total = len(library)
    read_books = sum(book['read'] for book in library)
    percentage = (read_books / total * 100) if total > 0 else 0
    print(f"📊 Total books: {total}")
    print(f"✅ Books read: {read_books} ({percentage:.2f}%)")

# Main menu
def menu():
    while True:
        print("\n📘 Personal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_books()
        elif choice == '4':
            display_all_books()
        elif choice == '5':
            display_statistics()
        elif choice == '6':
            save_library()
            print("💾 Library saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    load_library()
    menu()
