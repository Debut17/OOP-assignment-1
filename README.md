# Library Management System (OOP)

## Project Overview
Refactored a procedural library management system into an object-oriented design using Python classes.

## Project Structure
library-management-oop\
│\
├── OOP-ASSIGNMENT-1\
│ ├── lms.py\
│ └── test.py


## Design Overview
### Book Class
- Attributes: id, title, author, total_copies, available_copies
- Methods: borrow(), return_book(), is_available()

### Member Class
- Attributes: id, name, email, borrowed_books
- Methods: borrow(), return_book(), list_books()

### Library Class
- Attributes: books (dict), members (dict), transactions (list)
- Methods: add_book(), add_member(), borrow(), return_book(), display methods

## Testing
- **Basic Operations**: Add, borrow, return, and display
- **Edge Cases**: Unavailable book, exceeding limit, returning unborrowed or invalid book/member

## How to Run
```bash
cd path
python test.py
