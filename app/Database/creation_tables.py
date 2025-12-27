import pymysql

# ---------- DB CONNECTION ----------
connection = pymysql.connect(
    host="mysql-feec659-riderkuldeep-91fe.i.aivencloud.com",
    user="avnadmin",
    password="",
    db="BloodBankDB",
    port=17255,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

try:
    cursor = connection.cursor()

    # ---------- USERS TABLE ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        type ENUM('user', 'agent') NOT NULL,
        mobile VARCHAR(15) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # ---------- STOCK TABLE ----------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock (
        id INT AUTO_INCREMENT PRIMARY KEY,
        blood_group ENUM(
            'A+', 'A-',
            'B+', 'B-',
            'AB+', 'AB-',
            'O+', 'O-'
        ) NOT NULL UNIQUE,
        units_available INT NOT NULL DEFAULT 0,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ON UPDATE CURRENT_TIMESTAMP
    )
    """)

    # ---------- INSERT USERS ----------
    insert_user = """
    INSERT IGNORE INTO users (name, email, password, type, mobile)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(insert_user, (
        "Rahul Sharma",
        "rahul@gmail.com",
        "rahul123",
        "user",
        "9876543210"
    ))

    cursor.execute(insert_user, (
        "john",
        "john@gmail.com",
        "john123",
        "admin",
        "9123456780"
    ))

    # ---------- INSERT STOCK ----------
    insert_stock = """
    INSERT IGNORE INTO stock (blood_group, units_available)
    VALUES (%s, %s)
    """

    blood_groups = [
        ('A+', 0), ('A-', 0),
        ('B+', 0), ('B-', 0),
        ('AB+', 0), ('AB-', 0),
        ('O+', 0), ('O-', 0)
    ]

    cursor.executemany(insert_stock, blood_groups)

    # ---------- VERIFY USERS ----------
    print("\nUSERS TABLE:")
    cursor.execute("SELECT id, name, email, type FROM users")
    for row in cursor.fetchall():
        print(row)

    # ---------- VERIFY STOCK ----------
    print("\nSTOCK TABLE:")
    cursor.execute("SELECT blood_group, units_available FROM stock")
    for row in cursor.fetchall():
        print(row)

finally:
    connection.close()
