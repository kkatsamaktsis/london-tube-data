import json
import pymysql

data = ''
with open('./train-network.json') as f:
    data = json.load(f)

db = pymysql.connect(host="localhost", user="root", password="qhj38!@unSpY", database="tube")

cursor = db.cursor()

station_insert_stmt = 'INSERT INTO stations(id, station_name, longitude, latitude) VALUES ("{}", "{}", {}, {})'

line_insert_stmt = 'INSERT INTO tube_lines(line_name) VALUES ("{}")'

line_station_insert_stm = 'INSERT INTO line_stations(line_id, station_id) VALUES ({}, "{}")'

for station in data['stations']:
    # Executing the SQL command
    insert_stmnt = station_insert_stmt.format(station['id'], station['name'], station['longitude'], station['latitude'])
    # print(insert_stmnt)
    cursor.execute(insert_stmnt)
    # Commit changes in the database
    db.commit()

for line in data['lines']:
    insert_stmnt = line_insert_stmt.format(line['name'])
    # print(insert_stmnt)
    cursor.execute(insert_stmnt)
    db.commit()

for (line_id, line) in enumerate(data['lines']):
    for station_id in line['stations']:
        insert_stmnt = line_station_insert_stm.format(line_id + 1, station_id)
        # print(insert_stmnt)
        cursor.execute(insert_stmnt)
        db.commit()

print("Data inserted.")

# Closing the connection
db.close()
