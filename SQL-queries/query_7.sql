SELECT groups.name, subjects.subject_name, grades.grade
FROM groups
JOIN students ON students.group_id = groups.name
JOIN grades ON grades.student_id = students.id
JOIN subjects ON subjects.id = grades.subject_id
WHERE groups.name = '9082'
AND subjects.subject_name = 'Company secretary'