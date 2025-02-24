import  mysql.connector


#insert,update,delete


insert_query='insert into student values(102,"Deepak")'
update_query='update student set sname="Deepak" where sid=102;'
delete_query='delete from student where sid=101;'



try:
    con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="root",database="niteshdb")

    curs = con.cursor() ##cursor is a buffer through which we execute statements

    curs.execute(insert_query) # execute query with cursor
    curs.execute(update_query)
    curs.execute(delete_query)
    con.commit()  # commit the transaction
    con.close()

    print("Finished.............")
except:
    print("connection unsuccessful")




