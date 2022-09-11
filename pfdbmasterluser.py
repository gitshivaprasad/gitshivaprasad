import sqlite3

conn = sqlite3.connect('Database22.db')
print "Opened database successfully";

conn.execute('CREATE TABLE MASTERUSER (UNAME CHAR(20) NOT NULL, UPWD CHAR(8),PRIMARY KEY (UNAME));')
print "Table created sucessfully";

conn.close()
