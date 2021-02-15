from flask import Flask, render_template
import mysql.connector
import pymysql

app = Flask(__name__)

test_db = pymysql.connect(
    host="sql3.freesqldatabase.com",
    user="sql3393154",
    password="p3tsfT6ePr",
    database="sql3393154"
)

cursor = test_db.cursor()

cursor.execute("CREATE TABLE people IF NOT EXISTS (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(150), lastname VARCHAR(150))")
sql = "INSTERT INTO customers (firstname, lastname) VALUES (%s, %s)"
val = [
    ("Tomas", "Brejl")
    ("Lucie", "Brejlova")
]

cursor.executemany(sql, val)

mydb.commit()

@app.route('/')
def hello_world():
    sql = "SELECT firstname FROM people"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template('index.html', list=result)

if __name__ == "__main__":
    app.run(host='localhost', port = 23465)