from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = "flash message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'student_database'


mysql = MySQL(app)

@app.route('/')
def Index():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', students=data)



@app.route('/insert', methods=['POST'])
def insert():

    if request.method == "POST":
        flash('Data Inserted Successfully')

        First_name = request.form['First Name']
        Last_name = request.form['Last Name']
        Email = request.form['Email']
        Phone_Number = request.form['Phone Number']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO students  (First_name, Last_name, Email, Phone_Number) VALUES(%s, %s, %s, %s)', (First_name, Last_name, Email, Phone_Number))
        mysql.connection.commit()
        return redirect(url_for('Index'))

