from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'students_db'
}

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students;")
        students = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', students=students)
    except mysql.connector.Error as err:
        return f"Error connecting to the database: {err}"

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        email = request.form['email']

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (first_name, last_name, age, email) VALUES (%s, %s, %s, %s)",
                           (first_name, last_name, age, email))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('home'))
        except mysql.connector.Error as err:
            return f"Error inserting data: {err}"

    return render_template('insert.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id = %s;", (id,))
        student = cursor.fetchone()
        cursor.close()
        conn.close()

        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            age = request.form['age']
            email = request.form['email']

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET first_name = %s, last_name = %s, age = %s, email = %s WHERE id = %s",
                           (first_name, last_name, age, email, id))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('home'))

        return render_template('update.html', student=student)
    except mysql.connector.Error as err:
        return f"Error fetching data for update: {err}"

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s;", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('home'))
    except mysql.connector.Error as err:
        return f"Error deleting data: {err}"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

