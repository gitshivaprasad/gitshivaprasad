from flask import Flask, render_template, url_for, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
      return render_template('home1.html')

@app.route('/searchstd')
def searchstd():
     return render_template('student2.html')

@app.route('/sear_rec', methods = ['POST','GET'])

def sear_rec():

       if request.method == 'POST':

              STD_ID = request.form['STD_ID']
              con = sql.connect("database22.db")
              con.row_factory = sql.Row
              cur = con.cursor()
##              cur.execute("select * from student WHERE STD_ID = ('STD_ID');")
              cur.execute("SELECT * FROM student WHERE STD_ID = 5555")
   ##           print(next(cur))

              if cur:
                    print("data retrived")
                    print(STD_ID)
                    print(cur.fetchall())
              else:
                    print("data search failed")


              rows = cur.fetchall();
              print(rows)
              return render_template("list1.html", rows = rows )
              con.close()

if __name__ == '__main__':
       app.run(debug = True )

