SELECT avg(grades.grade)
FROM teachers
JOIN subjects ON subjects.teacher_id = teachers.id
JOIN grades ON grades.subject_id = subjects.id
WHERE teachers.name = 'Jessica Watts'