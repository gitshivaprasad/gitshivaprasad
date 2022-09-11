from flask import Flask, render_template, url_for, request,redirect
import sqlite3 as sql



app = Flask(__name__)


@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/loghome', methods = ['POST','GET'])  
def loghome():
      if request.method == 'POST':
               
                    
              uname = request.form['slog']
              upwd = request.form['pstd']
              
              if (uname == 'OMPC' and upwd == 'Admin'):
                 return render_template("home.html")
              elif (uname == 'user1' and upwd == 'user123'):
                 return render_template("home.html")
              else:
                  return render_template('result2.html', msg = "login failed" )
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/searchstd')
def searchstd():
  return render_template('student2.html')

@app.route('/sear_rec', methods = ['POST','GET'])
 
def sear_rec():
    
   if request.method == 'POST':
       
      
           std_id = request.form['STD_ID']
           
           con = sql.connect("database22.db")
           con.row_factory = sql.Row
           cur = con.cursor()
           cur.execute("SELECT * FROM student WHERE STD_ID = ?", (std_id,))
           rows = cur.fetchall()
           print (rows)
           msg = "Record search sucessfully"
           return render_template("list.html", rows = rows )
           
        
##   else:
##           con.rollback()
           std_id = request.args.get('STD_ID')
##           msg = "Error in insert operation"
##           return render_template('result1.html', msg = msg )
           con.close()  

@app.route('/delstd')
def delstd():
  return render_template('student3.html')
          
@app.route('/delstd_rec', methods = ['POST','GET'])

def delstd_rec():

      if request.method == 'POST':
        std_id = request.form['STD_ID']
    	con = sql.connect("database22.db")
    	con.row_factory = sql.Row
    	cur = con.cursor()
        cur.execute("DELETE FROM student where std_id = ?", (std_id,))
        con.commit()
        con.close()
        msg = "Record deleted sucessfully "
        return render_template('result.html',msg = msg )
        con.close()  
             

@app.route('/enternew')
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


@app.route('/list')
def list():
   con = sql.connect("database22.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from student;")
   rows = cur.fetchall()
   
   return render_template("list.html", rows = rows )

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
      

if __name__ == '__main__':
    app.run(debug = True ) 
    
