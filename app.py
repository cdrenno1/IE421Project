#app.py
from flask import Flask, render_template
from db import get_db

app = Flask(__name__)

    #Show all pitcher data
@app.route('/')
def index():
     conn = get_db()
     try:
         with conn.cursor() as cursor:
             cursor.execute("select * FROM pitchers")
             pitchers = cursor.fetchall()
             print(cursor.rowcount)
     finally:
         conn.close()
     return render_template('homebrew.html', pitchers = pitchers)
            
# if __name__ == '__main__': 