def insert_dummy_data_into_employeess():
    cur.execute("insert into employeess (fname, lname) select left(md5(i::varchar),10) as fname,right(md5(i::varchar),10) as lname from generate_series(1, 500) s(i)")
    conn.commit()
    cur.execute("SELECT * FROM employeess")
    print("Results:")
    print (cur.description)
    print("\n\n Formatted Results:")
    for row in cur:
        print (row)


insert_dummy_data_into_employeess()