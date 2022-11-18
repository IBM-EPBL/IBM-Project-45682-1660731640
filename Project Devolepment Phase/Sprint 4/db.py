import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "expense_tracker"
)

mycursor = mydb.cursor()

# code to delete all frm - DELETE FROM table_name;
'''
sql="INSERT INTO PETA_USER(userid,email,password,wallet) VALUE(%s,%s,%s,%s)"
val = (userid,email,password,wallet)
mycursor.execute(sql, val)
'''
email="srini@gmail.com"
password="123456s"
sql = "SELECT * FROM peta_user WHERE email =%s AND password =%s"
val=(email,password)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()

mydb.commit()

