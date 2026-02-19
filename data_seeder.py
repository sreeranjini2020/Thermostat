import mysql.connector
from datetime import datetime, timedelta
import random
import time


# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",        
    user="root",             
    password="mysql2026",
    database="home_thermostat_db"
)

# Create a cursor
cursor = connection.cursor()

# Drop tables if they already exist
for i in range(1, 4):
    cursor.execute(f"DROP TABLE IF EXISTS thermostat_{i}")
    print(f" thermostat_{i} — dropped if existed")
connection.commit()

# Create 3 tables
for i in range(1, 4):
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS thermostat_{i}(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   time DATETIME DEFAULT CURRENT_TIMESTAMP,
                   humidity FLOAT NOT NULL,
                   temperature FLOAT NOT NULL)""")
connection.commit()

# Insert random data
def generate_random_data():
    rows = ()
    humidity = round(random.uniform(30.0, 90.0), 2)
    temperature = round(random.uniform(15.0, 35.0), 2)
    rows +=(humidity, temperature)
    print("Temperature and humidity sampled")  
    return rows


while True:
  for i in range(1,4):
     data = generate_random_data()
     cursor.execute(f"INSERT INTO thermostat_{i} (humidity, temperature) VALUES (%s, %s)", data)
     
  connection.commit()
  time.sleep(1)
# data1 = generate_random_data()
# cursor.execute("INSERT INTO thermostat_1 (humidity, temperature) VALUES (%s, %s)", data1)

# data2 = generate_random_data()
# cursor.execute("INSERT INTO thermostat_2 (humidity, temperature) VALUES (%s, %s)", data2 )

# data3 = generate_random_data()
# cursor.execute("INSERT INTO thermostat_3 (humidity, temperature) VALUES (%s, %s)", data3 )
# connection.commit()

# Insert into each table

# for i in range(1, 4):
#     data = generate_random_data(400)
#     cursor.executemany(
#         f"INSERT INTO thermostat_{i} (time, humidity, temperature) VALUES (%s, %s, %s)",
#         data
#     )
#     connection.commit()
#     print(f"thermostat_{i} — 400 rows inserted successfully!")