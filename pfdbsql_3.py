from flask import Flask, render_template, url_for, request, redirect
import sqlite3 as sql



app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home1.html')

@app.route('/app_std1')
def app_std1():
  return render_template('studentapp_sear.html')

@app.route('/app_std2', methods = ['POST','GET'])
 
def app_std2():
    
   if request.method == 'POST':
       
      
           std_id = request.form['STD_ID']
           con = sql.connect("database22.db")
           con.row_factory = sql.Row
           cur = con.cursor()
           cur.execute("SELECT * FROM student WHERE STD_ID = ?", (std_id,))
           rows = cur.fetchall()
           msg = "Record search sucessfully"
           return render_template("studentapp.html", rows = rows )
##           con.close()
   else:
           msg = "Record Not found"
           return redirect(url_for('std1'))

@app.route('/rec', methods = ['POST','GET'])

def appstd_rec():

      if request.method == 'POST':

         ADM_NO = request.form['ADM_NO']
         STD_ID = request.form['STD_ID']
         STD_NAM = request.form['STD_NAM']
         STD_FNA = request.form['STD_FNA']
         STD_SEX = request.form['STD_SEX']
         STD_CLA = request.form['STD_CLA']
         STD_SEC = request.form['STD_SEC']
         STD_JDT = request.form['STD_JDT']
   	 con = sql.connect("database22.db")
    	 con.row_factory = sql.Row
    	 cur = con.cursor()
         cur.execute("UPDATE student Set ADM_NO = ?,STD_NAM = ?,STD_FNA = ?,STD_SEX = ?, STD_CLA = ?,STD_SEC = ?,STD_JDT = ?" "WHERE STD_ID = ?", (ADM_NO,STD_NAM,STD_FNA,STD_SEX,STD_CLA,STD_SEC,STD_JDT,STD_ID) )
         con.commit()
         con.close()
         msg = "Record changed sucessfully "
         return render_template('result.html', msg = msg )
           
@app.route('/enterdel')
def new_student():
  return render_template('student1.html')

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




if __name__ == '__main__':
    app.run(debug = True ) 
    
