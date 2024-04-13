# status include pending, paid and cancelled.
# When create a bill, status will be "pending"
from connection import connect_to_postgresql


def create_bill(conn):
    cur = conn.cursor()
    member_id = input("Enter member ID: ")
    amount = input("Enter amount: ")
    bill_type = input("Enter bill type ('Registration Fee', 'Session Fee'): ")
    try:
        cur.execute("INSERT INTO bills (member_id, amount, status, bill_type) VALUES (%s, %s, 'Pending', %s);",
                    (member_id, amount, bill_type))
        conn.commit()
        print(f"Bill for Member ID: '{member_id}' created successfully.")
    except Exception as error:
        print(f"Error: {error}")


def update_bill_status(conn):
    cur = conn.cursor()
    # show all the bills of this member by search member's ID
    member_id = input("Enter member ID: ")
    cur.execute("""SELECT bill_id, amount, status, bill_type, created_at, updated_at FROM bills WHERE member_id = %s""",(member_id))
    bills = cur.fetchall()
    if not bills:
        print("No bills found for this member.")
        return
    for bill in bills:
        print(f"Bill ID: {bill[0]}, Amount: {bill[1]}, Status: {bill[2]}, Type: {bill[3]}, Created At: {bill[4]}, Updated At: {bill[5]}")

    bill_id = input("select the bill ID you want to update status: ")
    print("Select the status you want to update to")
    print("1. Paid")
    print("2. Pending")
    print("3. Cancelled")
    status_choice = input()

    status_map = {'1': 'Paid', '2': 'Pending', '3': 'Cancelled'}
    selected_status = status_map.get(status_choice, None)

    try:
        cur.execute(
            "UPDATE bills SET status = %s, updated_at = CURRENT_TIMESTAMP WHERE bill_id = %s RETURNING bill_id;",
            (selected_status, bill_id))
        updated_bill_id = cur.fetchone()[0]
        conn.commit()
        print(f"Bill with ID {updated_bill_id} has been successfully updated to '{selected_status}'.")
    except Exception as error:
        print(f"Error updating bill status: {error}")


if __name__ == "__main__":
     conn = connect_to_postgresql()
     #create_bill(conn)
     update_bill_status(conn)
