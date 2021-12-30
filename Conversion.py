#code to convert sql file into csv file
import sqlite3 as sql
import os
import csv
from sqlite3 import Error

try:
    conn=sql.connect('userdata.db')
    cursor = conn.cursor()
    cursor.execute("select * from record")
    with open("review.csv", "w",newline = '') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
        csv.writer(f, lineterminator='\n')


    dirpath = os.getcwd() + "/review.csv"
    print("Data exported Successfully into {}".format(dirpath))

except Error as e:
  print(e)

    
# Close database connection
finally:
  conn.close()