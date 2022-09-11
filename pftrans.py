import sqlite3

conn = sqlite3.connect('Database22.db')
print "Opened database successfully";


conn.execute('CREATE TABLE FTRANS (STD_RVOC INTEGER PRIMARY KEY AUTOINCREMENT, ADM_NO INT NOT NULL, STD_ID INT NOT NULL, STD_NAM CHAR(25), STD_FNA CHAR(25), STD_SEX CHAR(1),\
                     STD_CLA INT(2), STD_SEC CHAR(1), STD_FDat DATE, STD_FEE  REAL CHECK(STD_FEE >0), STD_REM CHAR(25));')

print "Table created sucessfully";

conn.close()
