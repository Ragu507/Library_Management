# Library Management System

This project is a Django-based web application designed to manage a library system. It allows for managing books, members, book instances, and loans. The project implements various features such as creating, updating, and deleting books, members, and loan records.

## Features

- **Book Management**: List, view, create, update, and delete books.
- **Member Management**: List, view, create, update, and delete library members.
- **Loan Management**: List, view, create, update, and delete loan records for book borrowing.
- **Book Instance Management**: Manage physical copies of books and their availability status.
- **Dashboard**: A summary view showing the number of books, instances, and their statuses (available or on loan).
- **User Creation for Members**: When creating a new member, a corresponding user is also created.

## Views

### Book Views
- **BookListView**: Displays a list of books, including the number of available copies.
- **BookDetailView**: Displays details about a specific book.
- **BookCreateView**: Form to create a new book.
- **BookUpdateView**: Form to update an existing book.
- **BookDeleteView**: Confirmation view for deleting a book.

### Member Views
- **MemberListView**: Displays a list of members.
- **MemberDetailView**: Displays details about a specific member.
- **MemberCreateView**: Form to create a new member along with a user account.
- **MemberUpdateView**: Form to update a member's information.
- **MemberDeleteView**: Confirmation view for deleting a member.

### Loan Views
- **LoanListView**: Displays a list of loan records.
- **LoanCreateView**: Form to create a new loan.
- **LoanUpdateView**: Form to update an existing loan.
- **LoanDeleteView**: Confirmation view for deleting a loan record.

### Book Instance Views
- **BookInstanceListView**: Displays a list of book instances (physical copies of books).
- **BookInstanceDetailView**: Displays details about a specific book instance.
- **BookInstanceCreateView**: Form to create a new book instance.
- **BookInstanceUpdateView**: Form to update a book instance.
- **BookInstanceDeleteView**: Confirmation view for deleting a book instance.

### Dashboard View
- **DashboardView**: Displays a summary of the library's books and their statuses, including the total number of books, available copies, and loans.

## Models

- **Book**: Represents a book with details like title, author, and ISBN.
- **Member**: Represents a library member.
- **Loan**: Represents a loan where a member borrows a book.
- **BookInstance**: Represents a physical copy of a book and its status (available, on loan, etc.).

## Forms

- **BookForm**: Form for creating and updating books.
- **MemberForm**: Form for creating and updating members.
- **LoanForm**: Form for managing loans.
- **BookInstanceForm**: Form for managing book instances.
- **UserCreationForm**: Custom form for creating users when registering members.

## URLs

You can define URL paths for these views in `urls.py` to navigate through the application. Example routes:
- `/books/` - List of books.
- `/books/<int:pk>/` - Book detail view.
- `/books/add/` - Add a new book.
- `/books/<int:pk>/edit/` - Update an existing book.
- `/books/<int:pk>/delete/` - Delete a book.
- Similarly, routes are available for members, loans, and book instances.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
