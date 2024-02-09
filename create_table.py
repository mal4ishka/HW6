import sqlite3


if __name__ == '__main__':
    sql_create_groups_table = """
    CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL
    );"""

    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
    );"""

    sql_create_teachers_table = """
        CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL);"""

    sql_create_subjects_table = """
        CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(255) NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    );"""

    sql_create_grades_table = """
        CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        grade DECIMAL(3, 1),
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
        );"""

    conn = sqlite3.connect('test.sqlite')
    cur = conn.cursor()

    # Виконання SQL-запиту
    cur.execute(sql_create_groups_table)
    cur.execute(sql_create_students_table)
    cur.execute(sql_create_teachers_table)
    cur.execute(sql_create_subjects_table)
    cur.execute(sql_create_grades_table)
