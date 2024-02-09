SELECT avg(grade)
FROM students
JOIN grades ON grades.student_id = students.id
JOIN subjects ON subjects.id = grades.subject_id
JOIN teachers ON teachers.id = subjects.teacher_id
WHERE students.name = 'Ricardo Olsen Jr.'
AND teachers.name = 'Jessica Watts'