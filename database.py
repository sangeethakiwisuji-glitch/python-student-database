import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT UNIQUE NOT NULL,
            course TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def add_student(name, roll_no, course):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, roll_no, course) VALUES (?, ?, ?)",
        (name, roll_no, course)
    )

    conn.commit()
    conn.close()

def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()
    return students

def search_student(roll_no):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    conn.close()
    return student
