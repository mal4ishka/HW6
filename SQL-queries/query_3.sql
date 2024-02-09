SELECT groups.name, avg(grades.grade)
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON subjects.id = grades.subject_id
JOIN groups ON groups.name = students.group_id
WHERE subject_name = 'Retail merchandiser'
GROUP BY 1