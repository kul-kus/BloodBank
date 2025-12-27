
import pymysql

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="BloodBankDB",
  host="mysql-feec659-riderkuldeep-91fe.i.aivencloud.com",
  password="",
  read_timeout=timeout,
  port=17255,
  user="avnadmin",
  write_timeout=timeout,
  autocommit=True   
)
  
try:
  cursor = connection.cursor()
  # cursor.execute("""CREATE TABLE mytest (id 
  # INTEGER PRIMARY KEY)""")

  cursor.execute(
      """
      INSERT INTO users (name, email, password, type, mobile)
      VALUES (%s, %s, %s, %s, %s)
      """,
      ("john", "john@gmail.com", "john123", "agent", "9123456780")
  )
#   cursor.execute("INSERT INTO mytest (id) VALUES (99090), (8080)")
#   cursor.execute("INSERT INTO mytest (id) VALUES (990902323), (2323)")

  cursor.execute("SELECT * FROM mytest")
  print(cursor.fetchall())
finally:
  connection.close()