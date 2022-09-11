from flask import Flask, render_template, url_for, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
  return render_template('student.html')

@app.route('/addrec', methods = ['POST','GET'])
 
def addrec():
    
    if request.method == 'POST':
       
       try:
         ADM_NO = request.form['ADM_NO']
         STD_ID = request.form['STD_ID']
         STD_NAM = request.form['STD_NAM']
         STD_FNA = request.form['STD_FNA']
         STD_SEX = request.form['STD_SEX']
         STD_CLA = request.form['STD_CLA']
         STD_SEC = request.form['STD_SEC']
         STD_JDT = request.form['STD_JDT']
       
         
         with sql.connect("database22.db") as con:
           cur = con.cursor()
           cur.execute("INSERT INTO student (ADM_NO, STD_ID, STD_NAM, STD_FNA, STD_SEX, STD_CLA, STD_SEC, STD_JDT) VALUES (?,?,?,?,?,?,?,?)", (ADM_NO,STD_ID,STD_NAM,STD_FNA,STD_SEX,STD_CLA,STD_SEC,STD_JDT) )
           con.commit()
           msg = "Record sucessfully added"

       except:
           con.rollback()
           msg = "Error in insert operation"

       finally:
           return render_template('result.html',msg = msg )
           con.close()  


@app.route('/list')
def list():
   con = sql.connect("database22.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from student;")
   rows = cur.fetchall()
   
   return render_template("list.html", rows = rows )

if __name__ == '__main__':
    app.run(debug = True ) 
    
