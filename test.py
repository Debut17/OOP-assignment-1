from lms import Library


lib = Library()

print("="*60)
print("LIBRARY MANAGEMENT SYSTEM (OOP TEST)")
print("="*60)

lib.add_book(1, "Python Crash Course", "Eric Matthes", 3)
lib.add_book(2, "Clean Code", "Robert Martin", 2)
lib.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)

lib.add_member(101, "Alice Smith", "alice@email.com")
lib.add_member(102, "Bob Jones", "bob@email.com")

lib.borrow(101, 1)
lib.borrow(101, 2)
lib.borrow(102, 1)

lib.display_available_books()
lib.display_member_books(101)

lib.return_book(101, 1)
lib.display_available_books()

lib.borrow(999, 1)
lib.return_book(101, 3)
lib.return_book(102, 999)

print("\nFinal transactions:")
lib.display_all_transactions()