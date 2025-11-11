# Library Management System - Procedural Style

books = []
members = []
borrowed_books = []

class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
        
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
    
    def get_info(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'available_copies': self.available_copies,
            'total_copies': self.total_copies
        }
        
    def is_available(self):
        return self.available_copies > 0
        
    def __str__(self):
        return f"Book(ID: {self.id}, Title: '{self.title}', Available: {self.available_copies}/{self.total_copies})"

class Member:
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print(f'Error: {self.name} has reached borrowing limit!')
            return False
        
        if not book.borrow():
            print(f"Error: '{book.title}' is unavailable!")
            return False

        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'")
        return True
    
    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"Error: {self.name} did not borrow '{book.title}'")
            return False
        
        self.borrowed_books.remove(book)
        book.return_book()
        print(f"{self.name} returned '{book.title}")
        return True
    
    def list_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"\nBook borrowed by {self.name}")
            for b in self.borrowed_books:
                print(f" - {b.title} by {b.author}")
                
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.transactions = []
    
    #Book Section    
    def add_book(self, book_id, title, author, total_copies):
        if book_id in self.books:
            print(f"Error: Book ID {book_id} already exists.")
            return
        book = Book(book_id, title, author, total_copies)
        self.books[book_id] = book
        print(f"Book: '{title} added successfully!'")
        
    def find_book(self, book_id):
        return self.books.get(book_id, None)
    
    #Member Section
    def add_member(self, member_id, name, email):
        if member_id in self.members:
            print(f"Error: Member ID {member_id} already exists.")
            return
        member = Member(member_id, name, email)
        self.members[member_id] = member
        print(f"Member '{name}' registered successfully!")
        
    def find_member(self, member_id):
        return self.members.get(member_id, None)

    #Borrow and Return
    def borrow(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not book:
            print(f"Error: Book not found!")
            return False
        
        if not member:
            print(f"Error: Member not found!")
            return False
        
        if member.borrow_book(book):
            self.transactions.append({
                'member_id': member_id,
                'book_id': book_id,
                'member_name': member.name,
                'book_title': book.title
            })
            return True
        return False
    
    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not book:
            print(f"Error: Book not found!")
            return False
        
        if not member:
            print(f"Error: Member not found!")
            return False
        
        if member.return_book(book):
            self.transactions = [
                t for t in self.transactions
                if not (t['member_id'] == member_id and t['book_id'] == book_id)
            ]
            return True
        return False
    
    def display_available_books(self):
        print(f"\n=== Available Books ===")
        for book in self.books.values():
            if book.is_available():
                print(book)
                
    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print(f"Error: Member not found!")
            return
        member.list_books()
        
    def display_all_members(self):
        print("\n=== All Members ===")
        for member in self.members.values():
            print(f"{member.name} ({len(member.borrowed_books)} books borrowed)")
            
    def display_all_transactions(self):
        print("\n=== Current Borrowed Books ===")
        for t in self.transactions:
            print(f"{t['member_name']} has '{t['book_title']}'")
