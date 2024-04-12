# COMP3005-Final-Project
Welcome to the Fitness Management System! This is a Python application that utilizes a PostgreSQL database. It is designed to streamline the operations of fitness centers and gyms by automating member management, class scheduling, maintenance tracking, and billing processes.
## Prerequisites:
Python 3.8 or higher  
PostgreSQL  
Pip for Python package installation  

## Setting up database:
Download and unzip the file  
Create a new database and name it at your convenience  
Copy the DDL query code to make up the table  
Copy the DML query code to insert sample data  

## Execution commands:
After setting up PostgreSQL start with our system!  
1. Open it via Pycharm or any other IDE by importing the project.   
2. *Then enter in the command line: pip install psycopg2-binary  
3. Run and executing the "main_menu.py"
4. Enter in the command line:  
   Enter database name: the name must be identical to the database name you have created  
   Enter your username and password for Postgres  
   Choose options in the menu to use the system  


## Execution notes (Please read before using the system):
For the classes, the trainer must select a day and a class and then send it to the staff, staff on their side choose the scheduled time on the selected date and book the room. The member’s page has the final scheduled class time and date. Therefore, members can view and book classes. When the member books a class, the class will not appear on the available class list until the member cancels the class.   

For the dashboard display menu, the member will only get their exercise routines, fitness achievements, and health statistics after they finish taking the classes. 


## Files:
1. Create_database_DDL.sql:  
A SQL script with commands to create the gym management system’s database structure, including tables and constraints.  
2. Sample_data_DML.sql:  
A script for inserting sample records into the database, allowing for initial functionality testing.  
3. ER Model: ER-diagram(JPG format):  
An image showing the entity-relationship model, which outlines the database entities and their relationships.  
4. Relational Schema: Relational_database_Schema(JPG format)  
A visual schema detailing the tables, columns, and relationships within the database.  

5. Implementation files:  
>>main_menu.py:  
The main interface for navigating the gym management application.  
connection.py:  
Manages the database connection.  
dashboard_display.py:  
Shows member-specific data like routines and stats.  
member_booking_classes.py:  
Handles booking and canceling of gym classes.  
member_management.py:  
Manages member accounts and personal information.  
staff_bills_management.py:  
Administers billing and payment records.  
staff_management.py:  
Manages gym class schedules and equipment maintenance.  
staff_room_booking.py:  
Manages booking of rooms for gym activities.  
trainer_management.py:  
Allows trainers to set schedules and view member info.  

## Authors: 
Ziyi Jiang 101266200
Zhimei Li 101258414
Yoli Li 101284913
