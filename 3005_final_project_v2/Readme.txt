Welcome to the Fitness Management System! This application is designed to streamline the operations of fitness centers and gyms by automating member management, class scheduling, maintenance tracking, and billing processes.
Video link
[https://youtu.be/i99Vwrvu7oo](https://youtu.be/i99Vwrvu7oo)
Prerequisites
* Python 3.8 or higher
* PostgreSQL
* Pip for Python package installation
Execution commands:
unzip the file
*Ensure PostgreSQL is installed and running on your system.
Create a new database and name it at your convenience.
Copy the DDL query code to make up the table.
Copy the DML query code to insert sample data.
After setting up PostgreSQL start with our system!
1. Enter database name: the name must be identical to the database name you have created
2. Enter your username and password for Postgres
3. Choose options in the menu to use the system


*Download python if you don't have it
*Then enter in the command line: pip install psycopg2-binary


This is a Python application that utilizes a PostgreSQL database. You can run it via Pycharm or any other IDE by importing the project and executing the "main_menu.py". 


Execution notes (Please read before using the system):
For the classes, the trainer must select a day and a class and then send it to the staff, staff on their side choose the scheduled time on the selected date and book the room. The member’s page has the final scheduled class time and date. Therefore, members can view and book classes. When the member books a class, the class will not appear on the available class list until the member cancels the class. For the dashboard display menu, the member will only get their exercise routines, fitness achievements, and health statistics after they finish taking the classes. The DML code inserted into the database includes three trainers, three staff, and two members(Assume the trainer and staff already know their ID). When trainer wants to find a member, they must know the member’s name to see their profile(The member must update their profile with their name). 


Files:
Create_database_DDL.sql:
* A SQL script with commands to create the gym management system’s database structure, including tables and constraints.
Sample_data_DML.sql:
* A script for inserting sample records into the database, allowing for initial functionality testing.
ER Model: ER-diagram(JPG format):
* An image showing the entity-relationship model, which outlines the database entities and their relationships.
Relational Schema: Relational_database_Schema(JPG format)
* A visual schema detailing the tables, columns, and relationships within the database.


Implementation files:
main_menu.py:
* The main interface for navigating the gym management application.
connection.py:
* Manages the database connection.
dashboard_display.py:
* Shows member-specific data like routines and stats.
member_booking_classes.py:
* Handles booking and canceling of gym classes.
member_management.py:
* Manages member accounts and personal information.
staff_bills_management.py:
* Administers billing and payment records.
staff_management.py:
* Manages gym class schedules and equipment maintenance.
staff_room_booking.py:
* Manages booking of rooms for gym activities.
trainer_management.py:
* Allows trainers to set schedules and view member info.


Authors: 
Ziyi Jiang 101266200
Zhimei Li 101258414
Yoli Li 101284913
