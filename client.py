import json
import pymysql

data = ''
with open('./train-network.json') as f:
    data = json.load(f)

db = pymysql.connect(host="localhost", user="root", password="[PASSWORD]", database="tube")

cursor = db.cursor()

while True:
    text = input("Select station ('station ...') OR line ('line ...') OR exit\n")  # Python 3
    
    if text == 'exit':
        break
    elif text[0:len('station')] == 'station':
        station_name = text.split(' ')[1]
        query = f"SELECT DISTINCT l.line_name FROM (line_stations AS l_s LEFT JOIN tube_lines AS l ON l_s.line_id = l.id" \
                f"  LEFT JOIN stations AS s ON l_s.station_id = s.id) WHERE s.station_name = '{station_name}';"
        # print(query)
        cursor.execute(query)
        res = cursor.fetchall()
        for l in res:
            print(l[0])
    elif text[0:len('line')] == 'line':
        line_name = text.split(' ')[1]
        query = f"SELECT DISTINCT s.station_name FROM (line_stations AS l_s LEFT JOIN tube_lines AS l ON l_s.line_id = l.id" \
                f" LEFT JOIN stations AS s ON l_s.station_id = s.id) WHERE l.line_name = '{line_name}';"
        # print(query)
        cursor.execute(query)
        res = cursor.fetchall()
        for l in res:
            print(l[0])
    else:
        print("Please insert a statement as formatted above.")

print("End.")

# Closing the connection
db.close()
