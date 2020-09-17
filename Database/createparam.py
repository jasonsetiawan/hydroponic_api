import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="daun_hijau"
)

cursor = db.cursor()
sql = "INSERT INTO data_tumbuhan (name, value) VALUES (%s, %s)"
values = [
  ("suhu", 0),
  ("kelembaban", 0),
  ("kelembabanTanah", 0),
  ("areaDaun", 0),
  ("pH", 0),
  ("ketinggianAir", 0)
]

for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data ditambahkan".format(len(values)))