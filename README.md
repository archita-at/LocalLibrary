# Local Library Management System
A web-based Library Management System built with Django that allows readers to browse books, borrow available copies, and enables staff members to manage the library catalog.


## Project Overview
This project simulates a real-world library management system with role-based access control. It provides functionality for readers to view and borrow books while allowing staff and administrators to manage books, authors, genres, and user permissions.

## Features
1. Reader Features
- Login and logout
- Browse books
- View book details
- View authors
- View borrowed books
2. Staff Features
- Manage books
- Manage book instances
- Manage authors
- Django admin access
3. Super User Features
- User management
- Permission management
- Full administrative access

## User Roles
| **User Role** | **Permissions** |
| :--- | :--- |
| Reader | View and borrow books |
| Super user | Manage library catalog |
| Staff user | Full system access |

## Technology Stack
- Backend: Django
- Database: SQLite
- Frontend: HTML, CSS, Bootstrap
- Authentication: Django Authentication System

## Database Models
| **Model** | **Description** |
| :--- | :--- |
| Book | Stores book information |
| Author | Stores author details |
| Genre | Stores book categories |
| Book Instance | Individual copy of a book |
| User | System users |

## Installation
1. Clone Repository
`git clone <repository-url>`
2. Create Virtual Environment
`python -m venv .venv`
3. Activate Environment
`source .venv/bin/activate`
4. Install dependencies
`pip install -r requirements.txt`
5. Apply Migrations
`python manage.py migrate`
6. Run Application
`python manage.py runserver`

## Testing
The application is accompanied by a Playwright automation framework that validates critical user workflows such as authentication, book management, and role-based access control.
[Playwright Test Automation Scripts](https://github.com/archita-at/LocalLibrary-Automation)
