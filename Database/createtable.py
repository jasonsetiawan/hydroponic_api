import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="daun_hijau"
)

cursor = db.cursor()
sql = """CREATE TABLE data_tumbuhan (
  name VARCHAR(255),
  value Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel berhasil dibuat!")