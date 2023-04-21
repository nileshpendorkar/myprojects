import mysql.connector as conn
def dbb():
    my_db=conn.connect(host="localhost",username="root",password="nilesh1432")
    db_cur=my_db.cursor()
    db_cur.execute("create database if not exists new1")
    my_db.commit()
    db_cur.execute("create table if not exists new1.Hospital(nameoftablet varchar(45),referenceNo varchar(45),Dose varchar(45),NoOfTablets varchar(45),lot varchar(45),issuedate varchar(45),expdate varchar(45),dailydose varchar(45),storageadvice varchar(45),nhs varchar(45),patname varchar(45),dob varchar(45),addres varchar(45))")
    my_db.commit()
    print('creted')
dbb()