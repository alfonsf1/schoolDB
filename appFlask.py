from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

#Database connection
def get_db_connection():
    conn = psycopg2.connect(host='localhost', dbname='schoolDB', user='postgres', password='2813308004')
    return conn

@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students;')
    students = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(students)

@app.route('/students/<identifier>', methods=['GET'])
def get_student(identifier):
    conn = get_db_connection()
    cur = conn.cursor()
    print(identifier)
    cur.execute(f'SELECT * FROM students WHERE id = {int(identifier)};')
    students = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(students)

@app.route('/students_by_name/<identifier>', methods=['GET'])
def get_student_by_name(identifier):
    conn = get_db_connection()
    cur = conn.cursor()
    print(identifier)
    cur.execute(f'SELECT * FROM students WHERE name = {identifier};')
    students = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(students)

@app.route('/professors_classes', methods=['GET'])
def get_professors_classes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM classes RIGHT JOIN professors ON classes.professorId = professors.id;')
    students = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True) 

