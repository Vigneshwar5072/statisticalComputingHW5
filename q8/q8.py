def display_ten_records():
    cur.execute("SELECT * FROM employeess limit 10")
    print("\n\n Formatted Results:")
    for row in cur:
        print (row)


display_ten_records()

cur.close()
conn.close()