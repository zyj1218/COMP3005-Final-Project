from connection import connect_to_postgresql


# trainer can set the available time and preference class type;
# staff can decide the actual time and class type.
def trainer_schedule(conn, trainer_id):
    print("Choose a class you want to schedule:")
    cur = conn.cursor()
    try:
        cur.execute("SELECT class_id, class_name, complexity, price From classes")
        classes = cur.fetchall()
        if classes:
            for c in classes:
                print(f"ID: {c[0]}, Name: {c[1]}, Complexity: {c[2]}, price: {c[3]}")
            chosen_class_id = input("enter the ID of the class you want to schedule:")
            available_date = input("enter the available date in next week for the class(yy-mm-dd): ")
            class_type = input("enter the class type you prefer for the class(personal/group):")

            cur.execute("""INSERT INTO trainer_schedules (trainer_id, class_id, available_date, class_type) 
                        VALUES (%s, %s, %s, %s)""",
                        (trainer_id, chosen_class_id, available_date, class_type))
            conn.commit()
            print("Class scheduled successfully.")

        else:
            print("No classes to schedule.")

    except Exception as e:
        print("An error occurred:", e)


# need to join several tables
# use member's name to search
def view_member_profile(conn):
    cur = conn.cursor()
    try:
        name = input("Enter the member's name you want to view: ").strip()
        query = """
            SELECT 
                m.member_id, 
                m.email, 
                fg.goal_1, fg.goal_2, fg.goal_3, 
                hm.height, hm.weight, hm.BMI
            FROM 
                members m
            LEFT JOIN 
                fitness_goals fg ON m.member_id = fg.member_id
            LEFT JOIN 
                health_metrics hm ON m.member_id = hm.member_id
            WHERE 
                m.name = %s;
            """
        cur.execute(query, (name,))
        profile = cur.fetchone()

        if profile:
            print(f"Member ID: {profile[0]}, Email: {profile[1]}")
            print(f"Fitness Goals: {profile[2]}, {profile[3]}, {profile[4]}")
            print(f"Health Metrics: Height - {profile[5]} cm, Weight - {profile[6]} kg, BMI - {profile[7]}")
        else:
            print("No member found with that name.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    conn = connect_to_postgresql()
    #trainer_schedule(conn, 2)
    view_member_profile(conn)
