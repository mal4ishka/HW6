SELECT DISTINCT subject_name
FROM students
JOIN grades ON grades.student_id = students.id
JOIN subjects ON subjects.id = grades.subject_id
WHERE students.name = 'Dakota Shannon'