from connection import connect_to_postgresql


def member_classes_booking(conn, member_id):
    cur = conn.cursor()

    try:
        cur.execute("""
                SELECT fcs.final_schedule_id, fcs.class_type, c.class_name, fcs.start_time, fcs.end_time, fcs.class_date, c.price,
                        COALESCE((SELECT COUNT(*) FROM bookings WHERE final_schedule_id = fcs.final_schedule_id), 0) as current_bookings,
                        EXISTS(SELECT 1 FROM bookings WHERE final_schedule_id = fcs.final_schedule_id AND member_id = %s) as already_booked
                FROM final_class_schedules fcs
                JOIN classes c ON fcs.class_id = c.class_id
                ORDER BY fcs.class_date, fcs.start_time
            """, (member_id,))
        all_classes = cur.fetchall()

        if not all_classes:
            print("No classes are available.")
            return

        print("Available classes for booking:")
        for c in all_classes:
            final_schedule_id, class_type, class_name, start_time, end_time, class_date, class_price, current_bookings, already_booked = c

            #if already_booked is true, skip the nexted loop
            if already_booked:
                continue

            if class_type == "personal" and current_bookings == 0:

                print(
                    f"ID: {final_schedule_id}, Type: {class_type}, Name: {class_name}, "
                    f"Start: {start_time}, End: {end_time}, Date: {class_date}, Price: {class_price}\n"
                    f"-----------------------------------------------------------------------------------------------------")


            elif class_type == "group" and current_bookings < 5:
                print(
                    f"ID: {final_schedule_id}, Type: {class_type}, Name: {class_name}, "
                    f"Start: {start_time}, End: {end_time}, Date: {class_date}, Bookings: {current_bookings}/5, Price: {class_price}\n"
                    f"------------------------------------------------------------------------------------------------------")

        selected_class_id = int(input("Enter the ID of the class you want to book: "))
        if selected_class_id != 0:
            cur.execute("INSERT INTO bookings (member_id, final_schedule_id) VALUES (%s, %s) RETURNING booking_id",
                        (member_id, selected_class_id))
            booking_id = cur.fetchone()[0]  # Retrieve the generated booking_id from the INSERT operation

            # After selecting a class to book, ensure the selected_class_id matches the class_id
            class_price_query = "SELECT price FROM classes WHERE class_id = (SELECT class_id FROM final_class_schedules WHERE final_schedule_id = %s);"
            cur.execute(class_price_query, (selected_class_id,))
            class_price = cur.fetchone()[0]

            insert_bill_query = "INSERT INTO bills (booking_id, member_id, amount, status, bill_type) VALUES (%s, %s, %s, 'Pending', 'Class Fee');"
            cur.execute(insert_bill_query, (booking_id, member_id, class_price))
            conn.commit()
            print("Class booked and bill generated successfully.")

        else:
            print("No available classes at the moment.")

    except Exception as e:
        print(f"An error occurred: {e}")


def member_cancel_booking(conn, member_id):
    #     show all the bookings
    #     choose the booking ID you want to cancel
    #     delete this data
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT b.booking_id, fs.class_type, fs.class_date, fs.start_time, fs.end_time
            FROM bookings b
            JOIN final_class_schedules fs ON b.final_schedule_id = fs.final_schedule_id
            WHERE b.member_id = %s;
            """, (member_id,))
        bookings = cur.fetchall()

        if bookings:
            print("Your bookings:")
            for booking in bookings:
                print(
                    f"Booking ID: {booking[0]}, Class Type: {booking[1]}, Date: {booking[2]}, Time: {booking[3]} to {booking[4]}")
            booking_id_to_cancel = input("Enter the Booking ID you want to cancel: ")

            # First, attempt to delete the bill associated with the booking
            cur.execute("DELETE FROM bills WHERE booking_id = %s RETURNING bill_id;", (booking_id_to_cancel,))
            bill_result = cur.fetchone()
            if bill_result:
                print(f"Bill {bill_result[0]} associated with booking has been removed.")

            # Then delete the booking itself
            cur.execute("DELETE FROM bookings WHERE booking_id = %s AND member_id = %s RETURNING booking_id;",
                        (booking_id_to_cancel, member_id))
            booking_result = cur.fetchone()
            if booking_result:
                print(f"Booking {booking_result[0]} cancelled successfully.")
                conn.commit()
            else:
                print("Cancellation failed. Please check the Booking ID.")
        else:
            print("You have no bookings.")

    except Exception as e:
        conn.rollback()  # Rollback in case of any error
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    conn = connect_to_postgresql()
    member_classes_booking(conn, 1)
    #member_cancel_booking(conn, 1)
