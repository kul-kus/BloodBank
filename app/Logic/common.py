# This is a placeholder. You can replace it with DB validation later
# def check_login(username, password,type):
#     # Example: hard-coded credentials
#     return username == "admin" and password == "admin"


from Database.connect import get_connection

def check_login(username, password, user_type="user"):
    
   # Validate login from users table
    #Returns user dict if valid, None if invalid
    
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            SELECT * FROM users 
            WHERE email=%s AND password=%s AND type=%s
            """
            cursor.execute(sql, (username, password, user_type))
            user = cursor.fetchone()
            return user  # dict if found, None if not
    finally:
        conn.close()


def get_stock_data():
    
   # Get All the Blood Stocks present
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT blood_group, units_available FROM stock")
            return cursor.fetchall()   # list of dicts
    finally:
        conn.close()