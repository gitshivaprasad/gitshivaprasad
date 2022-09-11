from flask import Flask, render_template, url_for, request,redirect
import sqlite3 as sql



app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home1.html')

##@app.route('/searchstd')
##def searchstd():
##  return render_template('student2.html')
##
##        
##   else:
####           con.rollback()
##           std_id = request.args.get('STD_ID')
####           msg = "Error in insert operation"
####           return render_template('result1.html', msg = msg )
##           con.close()  

@app.route('/app_std1')
def app_std1():
  return render_template('studentapp_ser.html')

@app.route('/app_std2', methods = ['POST','GET'])
 
def app_std2():
    
   if request.method == 'POST':
       
      
           std_id = request.form['STD_ID']
           
           con = sql.connect("database22.db")
           con.row_factory = sql.Row
           cur = con.cursor()
           cur.execute("SELECT * FROM student WHERE STD_ID = ?", (std_id,))
           rows = cur.fetchall()
         ADM_NO = row[0]
         STD_ID = row[1]
         STD_NAM = row[2]
         STD_FNA = row[3]
         STD_SEX = row[4]
         STD_CLA = row[5]
         STD_SEC = row[6]
         STD_JDT = row[7]
   
           print (rows)
           msg = "Record search sucessfully"
           return render_template("studentapp.html", rows = rows )
           

          
@app.route('/appstd_rec', methods = ['POST','GET'])

def appstd_rec():

      if request.method == 'POST':
        std_id = request.form['STD_ID']
    	con = sql.connect("database22.db")
    	con.row_factory = sql.Row
    	cur = con.cursor()
        cur.execute("UPDATE student Set ADM_NO = ?,STD_NAM = ?,STD_FNA = ?,STD_SEX = ?, STD_CLA = ?,STD_SEC = ?,STD_JDT = ?" "WHERE std_id = ?", (ADM_NO,STD_NAM,STD_FNA,STD_SEX,STD_CLA,STD_SEC,STD_JDT,std_id) )
        con.commit()
        con.close()
        msg = "Record changed sucessfully "
        return render_template('studentapp.html',msg = msg )
        con.close()  
             

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


@app.route('/app_std')
def app_std():
   con = sql.connect("database22.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from student;")
   rows = cur.fetchall()
   
   return render_template("listapp.html", rows = rows )



if __name__ == '__main__':
    app.run(debug = True ) 
    
