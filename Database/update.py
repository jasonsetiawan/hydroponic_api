import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="daun_hijau"
)

#Dari Sensor
temp = 28
hum = 57
soil_hum = 0
leaf = 1
ph = 15
level = 100


#DB Params
params = ["suhu","kelembaban","kelembabanTanah","areaDaun", "pH", "ketinggianAir"]
vals = [temp, hum, soil_hum, leaf, ph, level]

cursor = db.cursor()
sql = "UPDATE data_tumbuhan SET value=%s WHERE name=%s"
for i in range (6):
    val = (vals[i], params[i])
    cursor.execute(sql, val)

db.commit()

print("{} data diubah".format(cursor.rowcount))