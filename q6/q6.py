import subprocess
import sys
import psycopg2
#tweak the database parameters to match your specific postgres database.
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="welcome$1234", 
                        database="postgres")
cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE employeess (id SERIAL PRIMARY KEY,fname VARCHAR(10),lname VARCHAR(10));")
    conn.commit()
    cur.execute("SELECT * FROM employeess")
    print("employeess table created successfully:")
    print (cur.description)


create_table()


