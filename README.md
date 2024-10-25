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

3. Database Configuration

Open `database.py` and update the following fields with your MySQL credentials:

    host="localhost"

    user="your_username"

    password="your_password"

    database="laundry_management_db"

4. Run the Application
   Execute laundry.py to start the GUI:
   `python laundry.py`


## Step-by-Steps Instructions for seeing data in mysql from terminal-
  1. Log into MySQL:`mysql -u root -p`
  2. Create the Database: `CREATE DATABASE laundry_management_db;`
  3. Grant Privileges to a User: `Replace your_username and your_password accordingly:`
     
    `GRANT ALL PRIVILEGES ON laundry_management_db.* TO 'your_username'@'localhost' IDENTIFIED BY 'your_password';`
  4. Apply the Privileges: `FLUSH PRIVILEGES;`
  5. Verify Database: To see your data, run:
     
         mysql -u root -p
     
         Enter password: [your_password]
     
         SHOW DATABASES;
     
         USE laundry_management_db;
     
         SELECT * FROM laundry;
  6. Exit MySQL: `EXIT;`


 ## Outputs: 

<img width="1277" alt="1" src="https://github.com/user-attachments/assets/0e206f4e-595b-436f-9261-c17820c14c29">

     






   









