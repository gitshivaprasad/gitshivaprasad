from flask import Flask, render_template, url_for, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
      
              con = sql.connect("database22.db")
              con.row_factory = sql.Row
             
              cur = con.cursor()
##              cur.execute("select * from student WHERE STD_ID = ('STD_ID');")
##              cur.execute("SELECT * FROM student WHERE STD_ID = 5555;")
              cur.execute("select * from student ORDER BY STD_ID")
            
              rows = cur.fetchall()
              
             
              return render_template("list1.html", rows = rows )
              con.close()

if __name__ == '__main__':
       app.run(debug = True )

