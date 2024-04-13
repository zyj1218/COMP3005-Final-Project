import connection


def show_class_schedules(conn):
    cur = conn.cursor()
    cur.execute("SELECT final_schedule_id, class_type, class_date, start_time, end_time FROM final_class_schedules")
    schedules = cur.fetchall()
    for schedule in schedules:
        print(f"ID: {schedule[0]}, Class Type:{schedule[1]}\n"
              f"Class Date:{schedule[2]}, Start Time:{schedule[3]}, End Time:{schedule[4]}\n"
              f"--------------------------------------------------------------------------")
    schedule_id = int(input("Select a schedule by ID: "))
    return schedule_id


def show_all_rooms(conn):
    cur = conn.cursor()
    cur.execute("SELECT room_id, room_name, features FROM rooms")
    rooms = cur.fetchall()
    for room in rooms:
        print(room)
    room_id = int(input("Select a room by ID: "))
    return room_id


def check_room_availability(conn, room_id, class_date, start_time, end_time):
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM room_bookings
    WHERE room_id = %s
    AND event_date = %s
    AND NOT (start_time >= %s OR end_time <= %s)
    """, (room_id, class_date, end_time, start_time))
    bookings = cur.fetchall()
    return len(bookings) == 0


def class_room_booking(conn, room_id, schedule_id):
    cur = conn.cursor()
    cur.execute("SELECT class_date, start_time, end_time FROM final_class_schedules WHERE final_schedule_id = %s",
                (schedule_id,))
    schedule = cur.fetchone()
    if schedule:
        class_date, start_time, end_time = schedule
        if check_room_availability(conn, room_id, class_date, start_time, end_time):
            cur.execute("INSERT INTO room_bookings (room_id, event_date, start_time, end_time) VALUES (%s, %s, %s, %s)",
                        (room_id, class_date, start_time, end_time))
            conn.commit()
            print("Room booked successfully.")
            print("The information has been sent to the members by mail.")
        else:
            print("Room is not available. Please choose another room.")
            room_id = show_all_rooms(conn)
            class_room_booking(conn, room_id, schedule_id)
    else:
        print("Schedule not found.")

def other_event_room_booking(conn, room_id):
    cur = conn.cursor()
    event_date = input("Enter the event date(yy-mm-dd): ")
    start_time = input("Enter the event start time(hh:mm): ")
    end_time = input("Enter the event end time(hh:mm): ")

    if check_room_availability(conn, room_id, event_date, start_time, end_time):
        cur.execute("INSERT INTO room_bookings (room_id, event_date, start_time, end_time) VALUES (%s, %s, %s, %s)",
                    (room_id, event_date, start_time, end_time))
        conn.commit()
        print("Room booked successfully.")
    else:
        print("Room is not available. Please choose another room.")
        room_id = show_all_rooms(conn)
        class_room_booking(conn, room_id)


if __name__ == "__main__":
    conn = connection.connect_to_postgresql()
    #schedule_id = show_class_schedules(conn)
    room_id = show_all_rooms(conn)
    other_event_room_booking(conn, room_id)

