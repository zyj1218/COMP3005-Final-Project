from connection import connect_to_postgresql
def display_exercise_routine(conn, member_id):
    cur = conn.cursor()
    try:
        cur.execute("""
        SELECT routine_1, routine_2, routine_3 
        From exercise_routines 
        Where member_id = %s;""", (member_id,))

        result = cur.fetchone()

        if result:

            print("Exercise Routines for member_id", member_id)
            print("Routine 1:", result[0])
            print("Routine 2:", result[1])
            print("Routine 3:", result[2])
        else:
            print("No routines found for member ID", member_id)

    except Exception as e:
        print("An error occurred:", e)

def display_achievements(conn, member_id):
    cur = conn.cursor()
    try:
        cur.execute("""
        SELECT a_1, a_2, a_3 
        From achievements 
        Where member_id = %s;""", (member_id,))

        result = cur.fetchone()

        if result:

            print("Achievements for member_id", member_id)
            print("Achievement 1:", result[0])
            print("Achievement 2:", result[1])
            print("Achievement 3:", result[2])
        else:
            print("No Achievements found for member_id", member_id)

    except Exception as e:
        print("An error occurred:", e)

def display_health_statistics(conn, member_id):
    cur = conn.cursor()
    try:
        cur.execute("""
        SELECT resting_heart_rate, average_daily_steps 
        From health_statistics 
        Where member_id = %s;""", (member_id,))

        result = cur.fetchone()

        if result:
            print("Health_statistics for member ID", member_id)
            print("Resting heart rate:", result[0])
            print("Average daily steps:", result[1])
        else:
            print("No statistics found for member_id", member_id)

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    conn = connect_to_postgresql()
    #display_exercise_routine(conn, 2)
    #display_achievements(conn, 2)
    #display_health_statistics(conn, 2)
