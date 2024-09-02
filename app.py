from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='krish@1613',
        database='placement_db'
    )
    return connection

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(students)

# Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)',
        (new_student['name'], new_student['email'], new_student['phone'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Student added successfully'}), 201

# Update an existing student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    updated_student = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'UPDATE students SET name=%s, email=%s, phone=%s WHERE student_id=%s',
        (updated_student['name'], updated_student['email'], updated_student['phone'], student_id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Student updated successfully'}), 200

# Delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM students WHERE student_id=%s', (student_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Student deleted successfully'}), 200

# Get all companies
@app.route('/companies', methods=['GET'])
def get_companies():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM companies')
    companies = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(companies)

# Add a new company
@app.route('/companies', methods=['POST'])
def add_company():
    new_company = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO companies (name, location) VALUES (%s, %s)',
        (new_company['name'], new_company['location'])
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Company added successfully'}), 201

# Update an existing company
@app.route('/companies/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    updated_company = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'UPDATE companies SET name=%s, location=%s WHERE company_id=%s',
        (updated_company['name'], updated_company['location'], company_id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Company updated successfully'}), 200

# Delete a company
@app.route('/companies/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM companies WHERE company_id=%s', (company_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Company deleted successfully'}), 200

# Render the dashboard
@app.route('/dashboard')
def dashboard():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.execute('SELECT * FROM companies')
    companies = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', students=students, companies=companies)

if __name__ == '__main__':
    app.run(debug=True)
