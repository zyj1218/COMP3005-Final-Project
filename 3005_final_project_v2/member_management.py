from connection import connect_to_postgresql


def register_member(conn):
    cur = conn.cursor()
    print("Welcome! Please create your account by input your username and password")
    username = input("Enter your username (Case sensitive): ")
    password = input("Enter your password: ")

    try:
        cur.execute("INSERT INTO members (username, password) VALUES (%s, %s) RETURNING member_id;",
                    (username, password))
        member_id = cur.fetchone()[0]
        conn.commit()
        print(f"Member registered successfully with ID {member_id}.")
    except Exception as error:
        print(f"Error: {error}")


def login_member(conn):
    username = input("Enter your username (Case sensitive): ")
    password = input("Enter your password: ")

    cur = conn.cursor()
    cur.execute("SELECT member_id FROM members WHERE username = %s AND password = %s", (username, password))
    result = cur.fetchone()

    if result:
        print("Login successful!")
        return result[0]  # because 'member_id' is the first column
    else:
        print("Login failed. Please check your credentials.")
        return None


def update_member_profile(conn, member_id):
    cur = conn.cursor()
    try:
        cur.execute("SELECT name, email FROM members WHERE member_id = %s;", (member_id,))
        member_data = cur.fetchone()
        if member_data:
            name, email = member_data
            print(f"Current Name: {name}")
            print(f"Current Email: {email}")
        else:
            print("Member not found.")
            return
    except Exception as e:
        print(f"Error fetching current profile data: {e}")
        return

    # Get the updated profile data from the user
    new_name = input("Enter your new name (or press Enter to keep current): ")
    new_email = input("Enter your new email (or press Enter to keep current): ")

    try:
        # Update the name if a new name was provided
        if new_name:
            cur.execute("UPDATE members SET name = %s WHERE member_id = %s;", (new_name, member_id))
        else:
            new_name = name  # Use the current name if no new name was provided
        
        # Update the email if a new email was provided
        if new_email:
            cur.execute("UPDATE members SET email = %s WHERE member_id = %s;", (new_email, member_id))
        else:
            new_email = email

        conn.commit()
        print(f"Profile updated successfully. New Name: {new_name}, New Email: {new_email}")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred during profile update: {e}")


def update_fitness_goals(conn, member_id):
    cur = conn.cursor()
    print("You can input 3 goals at most:")
    goal_1 = input("Enter your first goal: ")
    goal_2 = input("Enter your second goal: ")
    goal_3 = input("Enter your third goal: ")

    try:
        cur.execute("""
            INSERT INTO fitness_goals (member_id, goal_1, goal_2, goal_3)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (member_id) DO UPDATE
            SET goal_1 = EXCLUDED.goal_1,
                goal_2 = EXCLUDED.goal_2,
                goal_3 = EXCLUDED.goal_3;
        """, (member_id, goal_1, goal_2, goal_3))
        conn.commit()
        print("Your fitness goals updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_health_metrics(conn, member_id):
    cur = conn.cursor()

    height= input("Enter your height(cm): ")
    weight = input("Enter your weight(kg): ")
    BMI = input("Enter your BMI(Body Mass Index): ")

    try:
        cur.execute("""
            INSERT INTO health_metrics (member_id, height, weight, BMI)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (member_id) DO UPDATE
            SET height = EXCLUDED.height,
                weight = EXCLUDED.weight,
                BMI = EXCLUDED.BMI;
        """, (member_id, height, weight, BMI))
        conn.commit()
        print("Your health metrics updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def pay_bills(conn, member_id):
    cur = conn.cursor()
    cur.execute("SELECT bill_id, amount FROM bills WHERE member_id = %s AND status = 'Pending';", (member_id,))
    bills = cur.fetchall()

    if not bills:
        print("No pending bills.")
        return

    total_amount = sum(bill[1] for bill in bills)
    print(f"Total amount due: {total_amount}")
    pay_now = input("Do you want to pay all bills now? (yes/no): ")

    if pay_now.lower() == 'yes':
        delete_query = "DELETE FROM bills WHERE member_id = %s;"
        cur.execute(delete_query, (member_id,))
        conn.commit()
        print("Bills paid successfully and cleared.")
    else:
        print("Payment deferred.")


# if __name__ == "__main__":
#     conn = connect_to_postgresql()
#     update_health_metrics(conn,2)