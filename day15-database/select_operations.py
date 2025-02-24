import  mysql.connector


#insert,update,delete

select_query='select * from student;'



try:
    con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="root",database="niteshdb")

    curs = con.cursor() ##cursor is a buffer through which we execute statements

    curs.execute(select_query) # execute query with cursor

    #fetch data from cursor

    for row in curs:
        print(row[0],row[1])

    con.close()

    print("Finished.............")
except:
    print("connection unsuccessful")




