from member_booking_classes import member_classes_booking, member_cancel_booking
from member_management import pay_bills, register_member, login_member, update_member_profile, update_fitness_goals, \
    update_health_metrics
from connection import connect_to_postgresql
from dashboard_display import display_exercise_routine, display_achievements, display_health_statistics
from staff_bills_management import create_bill, update_bill_status
from staff_management import class_schedule_update, insert_maintenance_record, display_all_maintenance_records
from staff_room_booking import show_class_schedules, show_all_rooms, class_room_booking, other_event_room_booking
from trainer_management import trainer_schedule, view_member_profile

conn = connect_to_postgresql()


def main_menu():
    while True:
        print("1. Member")
        print("2. Trainer")
        print("3. Staff")
        print("4. Exit")
        role = input("Choose your role(number only): ")
        if role == "1":
            member_menu()
        elif role == "2":
            trainer_menu()
        elif role == "3":
            staff_menu()
        elif role == "4":
            print("Exiting the menu.")
            break


def member_menu():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        action = input("Choose an action: ")
        if action == "1":
            register_member(conn)
        elif action == "2":
            member_id = login_member(conn)
            if member_id:
                member_logged_in_menu(member_id)
        elif action == "3":
            print("Back to main menu to change your role")
            break


def member_logged_in_menu(member_id):
    while True:
        print("1. Update Member Profile")
        print("2. Update your Fitness Goals")
        print("3. Update your Health Metrics")
        print("4. Dashboard Display Menu")
        print("5. Book and Manage your classes")
        print("6. Pay your Bill")
        print("7. Exit")
        action = input("Choose an action: ")
        if action == "1":
            update_member_profile(conn, member_id)
        elif action == "2":
            update_fitness_goals(conn, member_id)
        elif action == "3":
            update_health_metrics(conn, member_id)
        elif action == "4":
            dashboard_display_menu(conn, member_id)
        elif action == "5":
            class_management_menu(conn, member_id)
        elif action == "6":
            pay_bills(conn, member_id)
        elif action == "7":
            print("Back to main menu to choose your role")
            break

def dashboard_display_menu(conn, member_id):
    while True:
        print("1. Display Exercise Routines")
        print("2. Display Fitness Achievement")
        print("3. Display Health Statistics")
        print("4. Exit")
        action = input("Choose an action: ")
        if action == "1":
            display_exercise_routine(conn, member_id)
        elif action == "2":
            display_achievements(conn, member_id)
        elif action == "3":
            display_health_statistics(conn, member_id)
        elif action == "4":
            print("Back to Member Menu")
            break


def class_management_menu(conn, member_id):
    while True:
        print("1. Book a class")
        print("2. Cancel a booking")
        print("3. Exit")
        action = input("Choose an action: ")
        if action == "1":
            member_classes_booking(conn, member_id)
        elif action == "2":
            member_cancel_booking(conn, member_id)
        elif action == "3":
            print("Back to Member Menu")
            break


# for trainer, we don't need they login the system, just input their ID is enough
def trainer_menu():
    trainer_id = input("Input your trainer ID: ")
    if validate_trainer_id(conn, trainer_id):
        trainer_management_menu(trainer_id)
    else:
        print("Invalid Trainer ID. Please try again.")

def validate_trainer_id(conn, trainer_id):
    cur = conn.cursor()
    try:
        cur.execute("SELECT EXISTS(SELECT 1 FROM trainers WHERE trainer_id = %s)", (trainer_id,))
        return cur.fetchone()[0]
    except Exception as e:
        print("An error occurred while validating trainer ID:", e)
        return False


def trainer_management_menu(trainer_id):
    while True:
        print("1. Schedule classes")
        print("2. View member profile")
        print("3. Exit")

        action = input("Choose an action: ")
        if action == "1":
            trainer_schedule(conn, trainer_id)
        elif action == "2":
            view_member_profile(conn)
        elif action == "3":
            print("Back to Main Menu to change your role")
            break


# for staffs, we don't need they login the system, just input their ID is enough
def staff_menu():
    staff_id = input("Input your staff ID: ")
    if validate_staff_id(conn, staff_id):
        staff_management_menu()
    else:
        print("Invalid Staff ID. Please try again.")

def validate_staff_id(conn, staff_id):
    cur = conn.cursor()
    try:
        cur.execute("SELECT EXISTS(SELECT 1 FROM staffs WHERE staff_id = %s)", (staff_id,))
        return cur.fetchone()[0]
    except Exception as e:
        print("An error occurred while validating staff ID:", e)
        return False


def staff_management_menu():
    while True:
        print("1. Update Class Schedule")
        print("2. Equipment Maintenance Monitoring")
        print("3. Room Booking")
        print("4. Billing Management")
        print("5. Exit")
        action = input("Choose an action: ")
        if action == "1":
            class_schedule_update(conn)
        elif action == "2":
            staff_equipment_menu(conn)
        elif action == "3":
            room_booking_menu(conn)
        elif action == "4":
            bill_menu(conn)
        elif action == "5":
            print("Back to Main Menu to change your role.")
            break

def staff_equipment_menu(conn):
    print("1. Insert a maintenance record")
    print("2. Display all maintenance records")

    action = input("Choose an action: ")
    if action == "1":
        insert_maintenance_record(conn)
    elif action == "2":
        display_all_maintenance_records(conn)


def room_booking_menu(conn):
    print("1. Book a room for scheduled training classes")
    print("2. Book a room for other events")

    action = input("Choose an action: ")
    if action == "1":
        schedule_id = show_class_schedules(conn)
        room_id = show_all_rooms(conn)
        class_room_booking(conn, room_id, schedule_id)

    elif action == "2":
        room_id = show_all_rooms(conn)
        other_event_room_booking(conn, room_id)


def bill_menu(conn):
    print("1. create a bill for a member")
    print("2. update a bill status")
    action = input("Choose an action: ")
    if action == "1":
        create_bill(conn)
    if action == "2":
        update_bill_status(conn)


if __name__ == "__main__":
    main_menu()
