from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_OF_STUDENTS = 50
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 10
NUMBER_OF_TEACHERS = 5
NUMBER_OF_GRADES = 1000


def generate_fake_data(number_of_groups, number_of_students, number_of_teachers, number_of_subjects,
                       number_of_grades) -> tuple:
    fake_groups = []
    fake_students = []
    fake_subjects = []
    fake_teachers = []
    fake_grades = []
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

    for _ in range(number_of_groups):
        fake_groups.append(fake_data.pyint())

    for _ in range(number_of_students):
        fake_students.append(fake_data.name())

    for _ in range(number_of_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_of_subjects):
        fake_subjects.append(fake_data.job())

    for _ in range(number_of_grades):
        fake_grades.append(randint(1, 100))

    return fake_groups, fake_students, fake_teachers, fake_subjects, fake_grades


def fill_groups(value):
    with sqlite3.connect('test.sqlite') as con:
        cur = con.cursor()
        sql_insert = f'INSERT INTO groups (name) VALUES ({value})'
        cur.execute(sql_insert)
        con.commit()


def fill_students(name, group_id):
    with sqlite3.connect('test.sqlite') as con:
        cur = con.cursor()
        sql_insert = f'INSERT INTO students (name, group_id) VALUES ("{name}", {group_id})'
        cur.execute(sql_insert)
        con.commit()


def fill_teachers(value):
    with sqlite3.connect('test.sqlite') as con:
        cur = con.cursor()
        sql_insert = f'INSERT INTO teachers (name) VALUES ("{value}")'
        cur.execute(sql_insert)
        con.commit()


def fill_subjects(subject_name, teacher_id):
    with sqlite3.connect('test.sqlite') as con:
        cur = con.cursor()
        sql_insert = f'INSERT INTO subjects (subject_name, teacher_id) VALUES ("{subject_name}", {teacher_id})'
        cur.execute(sql_insert)
        con.commit()


def fill_grades(student_id, subject_id, grade, timestamp):
    with sqlite3.connect('test.sqlite') as con:
        cur = con.cursor()
        sql_insert = f'INSERT INTO grades (student_id, subject_id, grade, timestamp) VALUES ({student_id}, {subject_id}, {grade}, {timestamp})'
        cur.execute(sql_insert)
        con.commit()


if __name__ == "__main__":
    groups, students, teachers, subjects, grades = generate_fake_data(NUMBER_OF_GROUPS, NUMBER_OF_STUDENTS,
                                                                      NUMBER_OF_TEACHERS, NUMBER_OF_SUBJECTS,
                                                                      NUMBER_OF_GRADES)
    # print(groups)
    # print(students)
    # print(teachers)
    # print(subjects)
    # print(grades)

    for group in groups:
        fill_groups(group)

    for student in students:
        fill_students(student, choice(groups))

    for teacher in teachers:
        fill_teachers(teacher)

    for subject in subjects:
        fill_subjects(subject, randint(1, NUMBER_OF_TEACHERS))

    for grade in grades:
        fill_grades(randint(1, NUMBER_OF_STUDENTS), randint(1, NUMBER_OF_SUBJECTS), grade,
                    int(faker.Faker().past_datetime().timestamp()))
