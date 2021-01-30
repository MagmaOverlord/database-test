from flask import Flask, render_template
import mysql.connector
import pymysql

app = Flask(__name__)

test_db = pymysql.connect(
    host="localhost",
    user="root",
    password="greatkid5000",
    database="sys"
)

cursor = test_db.cursor()

@app.route('/')
def hello_world():
    sql = "SELECT name FROM test"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template('index.html', list=result)

if __name__ == "__main__":
    app.run(host='localhost', port = 23465)