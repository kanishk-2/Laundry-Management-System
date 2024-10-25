# Laundry-Management-System

This is a simple Laundry Management System built using Python, Tkinter for the GUI, and MySQL as the database. The system allows users to manage laundry records by adding, updating, deleting, searching, and viewing all entries.

## Features

- Add new laundry entries with details such as `Laundry ID`, `Customer Name`, `Service Type`, `Contact`, `Address`, and `Status`.
- Update existing entries.
- Delete entries by `Laundry ID`.
- Search entries by `Laundry ID` or `Customer Name`.
- Display all laundry records in a table format.

## File Structure

- `database.py`: Handles database operations (connects to MySQL, creates tables, and defines CRUD functions).
- `laundry.py`: GUI application using Tkinter, which allows users to interact with the laundry management system.

## Requirements

- Python 3.x
- MySQL
- `mysql-connector-python` library for MySQL-Python interaction
- Tkinter (comes with Python standard library)

## Setup Instructions

1. **Install MySQL**  
   If not already installed, install MySQL. [MySQL Installation Guide](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)

2. **Install `mysql-connector-python`**
   ```bash
   pip install mysql-connector-python
