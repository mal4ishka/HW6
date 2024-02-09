SELECT students.name, avg(grades.grade)
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON subjects.id = grades.subject_id
WHERE subject_name = 'Retail merchandiser'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1