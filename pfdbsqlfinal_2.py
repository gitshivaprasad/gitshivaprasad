from flask import Flask, render_template, url_for, request,redirect
import sqlite3 as sql



app = Flask(__name__)


@app.route('/loginft')
def loginft():
   return render_template('loginft.html')

@app.route('/loghomeft', methods = ['POST','GET'])  
def loghomeft():
      if request.method == 'POST':
               
                    
              uname = request.form['slog']
              upwd = request.form['pstd']
              
              if (uname == 'OMPC' and upwd == 'Admin'):
                 return render_template("homeft.html")
              elif (uname == 'user1' and upwd == 'user123'):
                 return render_template("homeft.html")
              else:
                  return render_template('result2ft.html', msg = "login failed" )
@app.route('/')
def home():
   return render_template('homeft.html')

@app.route('/searchstdft')
def searchstdft():
  return render_template('student2ft.html')

@app.route('/sear_recft', methods = ['POST','GET'])
 
def sear_recft():
    
   if request.method == 'POST':
       
      
           std_id = request.form['STD_ID']
           
           con = sql.connect("database22.db")
           con.row_factory = sql.Row
           cur = con.cursor()
           cur.execute("SELECT * FROM ftrans;")
           rows = cur.fetchall()
           print (rows)
           msg = "Record search sucessfully"
           return render_template("listft.html", rows = rows )
           std_id = request.args.get('STD_ID')
           con.close()  


@app.route('/sear_recft1', methods = ['POST','GET'])
 
def sear_recft1():
    
   if request.method == 'POST':
       
      
           std_id = request.form['STD_ID']
           
           con = sql.connect("database22.db")
           con.row_factory = sql.Row
           cur = con.cursor()
           cur.execute("SELECT * FROM ftrams WHERE STD_ID = ?", (std_id,))
           rows = cur.fetchall()
           print (rows)
           msg = "Record search sucessfully"
           return render_template("listft.html", rows = rows )
           std_id = request.args.get('STD_ID')
           con.close()  

@app.route('/delstdft')
def delstdft():
  return render_template('student3ft.html')
          
@app.route('/delstd_recft', methods = ['POST','GET'])

def delstd_recft():

      if request.method == 'POST':
        std_id = request.form['STD_ID']
    	con = sql.connect("database22.db")
    	con.row_factory = sql.Row
    	cur = con.cursor()
        cur.execute("DELETE FROM ftrans where std_id = ?", (std_id,))
        con.commit()
        con.close()
        msg = "Record deleted sucessfully "
        return render_template('resultft.html',msg = msg )
        con.close()  
             

@app.route('/enternewft')
def new_studentft():
  return render_template('student1ft.html')

@app.route('/addrecft', methods = ['POST','GET'])
 
def addrecft():
    
    if request.method == 'POST':
       
       try:
         ADM_NO = request.form['ADM_NO']
         STD_ID = request.form['STD_ID']
         STD_NAM = request.form['STD_NAM']
         STD_FNA = request.form['STD_FNA']
         STD_SEX = request.form['STD_SEX']
         STD_CLA = request.form['STD_CLA']
         STD_SEC = request.form['STD_SEC']
         STD_FDAT = request.form['STD_FDAT']
         STD_FEE = request.form['STD_FEE']
         STD_REM = request.form['STD_REM']
       
         
         with sql.connect("database22.db") as con:
           cur = con.cursor()
           cur.execute("INSERT INTO ftrans (ADM_NO, STD_ID, STD_NAM, STD_FNA, STD_SEX, STD_CLA, STD_SEC, STD_FDAT, STD_FEE, STD_REM) VALUES (?,?,?,?,?,?,?,?,?.?)", (ADM_NO,STD_ID,STD_NAM,STD_FNA,STD_SEX,STD_CLA,STD_SEC,STD_FDAT, STD_FEE, STD_REM))
           con.commit()
           msg = "Record sucessfully added"

       except:
           con.rollback()
           msg = "Student ID already Exist in record,so operation not sucessfull"

       finally:
           return render_template('resultft.html',msg = msg )
           con.close()  


@app.route('/listft')
def listft():
   con = sql.connect("database22.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from ftrans;")
   rows = cur.fetchall()
   
   return render_template("listft.html", rows = rows )

@app.route('/app_std1ft')
def app_std1ft():
  return render_template('studentapp_searft.html')

@app.route('/app_std2ft', methods = ['POST','GET'])
 
def app_std2ft():
    
   if request.method == 'POST':
       
      
           std_id = request.form['STD_ID']
           con = sql.connect("database22.db")
           con.row_factory = sql.Row
           cur = con.cursor()
           cur.execute("SELECT * FROM ftrans WHERE STD_ID = ?", (std_id,))
           rows = cur.fetchall()
           msg = "Record search sucessfully"
           return render_template("studentapp.html", rows = rows )
##           con.close()
   else:
           msg = "Record Not found"
##           return redirect(url_for('std1'))
           return render_template('resultft.html', msg = msg )

@app.route('/recft', methods = ['POST','GET'])

def appstd_recft():

      if request.method == 'POST':

         ADM_NO = request.form['ADM_NO']
         STD_ID = request.form['STD_ID']
         STD_NAM = request.form['STD_NAM']
         STD_FNA = request.form['STD_FNA']
         STD_SEX = request.form['STD_SEX']
         STD_CLA = request.form['STD_CLA']
         STD_SEC = request.form['STD_SEC']
         STD_FDAT = request.form['STD_FDAT']
         STD_FEE = request.form['STD_FEE']
         STD_REM = request.form['STD_REM']
   	 con = sql.connect("database22.db")
    	 con.row_factory = sql.Row
    	 cur = con.cursor()
         cur.execute("UPDATE ftrans Set ADM_NO = ?,STD_NAM = ?,STD_FNA = ?,STD_SEX = ?, STD_CLA = ?,STD_SEC = ?, STD_FDAT= ?, STD_FEE= ?, STD_REM= ?" "WHERE STD_ID = ?", (ADM_NO,STD_NAM,STD_FNA,STD_SEX,STD_CLA,STD_SEC,STD_FDAT, STD_FEE, STD_REM,STD_ID) )
         con.commit()
         con.close()
         msg = "Record changed sucessfully "
         return render_template('resultft.html', msg = msg )
      

if __name__ == '__main__':
    app.run(debug = True ) 
    
