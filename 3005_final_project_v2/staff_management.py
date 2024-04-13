from connection import connect_to_postgresql


def class_schedule_update(conn):
    print("Choose a class you want to schedule a time:")
    cur = conn.cursor()
    try:
        cur.execute("""
                    SELECT ts.schedule_id, ts.trainer_id, ts.class_type, ts.available_date,
                           t.name, 
                           c.class_id, c.class_name
                    FROM trainer_schedules ts
                    LEFT JOIN trainers t ON ts.trainer_id = t.trainer_id 
                    LEFT JOIN classes c ON ts.class_id = c.class_id
                    """)
        trainer_schedules = cur.fetchall()

        if trainer_schedules:
            for t in trainer_schedules:
                print(f"Schedule ID: {t[0]}\nTrainer ID: {t[1]}, Trainer Name:{t[4]}\n"
                      f"Class ID: {t[5]}, Class Name:{t[6]}\n"
                      f"Preferred Class Type: {t[2]}\n"
                      f"Available Date: {t[3]}\n----------------------------")
            chosen_schedule_id = input("Enter the schedule ID of the class you want to update: ")
            confirmed_class_type = input("Enter the confirmed class type (personal/group): ")
            start_time = input("Enter the start time of the class (HH:MM): ")
            end_time = input("Enter the end time of the class (HH:MM): ")

            # Update trainer_schedules with the new class type
            cur.execute("""
                        UPDATE trainer_schedules
                        SET class_type = %s
                        WHERE schedule_id = %s
                        """, (confirmed_class_type, chosen_schedule_id))

            # Check if the schedule exists in final_class_schedules
            cur.execute("""
                        SELECT schedule_id
                        FROM final_class_schedules
                        WHERE schedule_id = %s
                        """, (chosen_schedule_id,))
            if cur.fetchone():
                # Update existing schedule
                cur.execute("""
                            UPDATE final_class_schedules
                            SET class_type = %s, start_time = %s, end_time = %s
                            WHERE schedule_id = %s
                            """, (confirmed_class_type, start_time, end_time, chosen_schedule_id))
            else:
                # Insert new schedule
                cur.execute("""
                            INSERT INTO final_class_schedules
                            (schedule_id, trainer_id, class_id, class_type, class_date, start_time, end_time)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """, (chosen_schedule_id, t[1], t[5], confirmed_class_type, t[3], start_time, end_time))

            conn.commit()
            print("Class schedule updated successfully.")
            print("The information has been sent to the members and trainers by mail.")

        else:
            print("No classes schedule to update.")

    except Exception as e:
        conn.rollback()  # Rollback in case of an error
        print("An error occurred:", e)



def insert_maintenance_record(conn):
    cur = conn.cursor()
    try:
        # show all the devices
        cur.execute("SELECT device_id, device_name, purchase_date fROM devices")
        devices = cur.fetchall()
        for device in devices:
            print(f"ID: {device[0]}, Name: {device[1]}, Purchase Date: {device[2]}")

        # Prompting staff for maintenance record details
        device_id = input("Enter the device ID you want to add a maintenance record: ")
        cur.execute("SELECT device_id FROM devices WHERE device_id = %s", (device_id,))

        maintenance_date = input("Enter the maintenance date (YYYY-MM-DD): ")
        next_maintenance_date = input("Enter the next maintenance date (YYYY-MM-DD): ")

        cur.execute("""
            INSERT INTO maintenance (device_id, maintenance_date, next_maintenance_date)
            VALUES (%s, %s, %s); """, (device_id, maintenance_date, next_maintenance_date))
        conn.commit()

        print("Maintenance record inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Join table devices and maintenance
# even some devices don't have a maintenance record. In this case, maintenance records will show NULL
def display_all_maintenance_records(conn):
    print("All devices maintenance records: ")
    cur = conn.cursor()
    cur.execute("""SELECT d.device_id, d.device_name, d.purchase_date, m.maintenance_date, m.next_maintenance_date 
                   FROM devices d
                   LEFT JOIN maintenance m ON d.device_id = m.device_id""")
    result = cur.fetchall()
    for r in result:
        device_id, device_name, purchase_date, maintenance_date, next_maintenance_date = r
        print(
            f"Device ID: {device_id}, Device Name: {device_name}, Purchase Date: {purchase_date}\n"
            f"Maintenance Date: {maintenance_date}, Next Maintenance Date: {next_maintenance_date}\n"
            f"_______________________________________________________________________________")


if __name__ == "__main__":
    conn = connect_to_postgresql()
    class_schedule_update(conn)
    # insert_maintenance_record(conn)
    #display_all_maintenance_records(conn)
