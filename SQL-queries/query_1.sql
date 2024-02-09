SELECT students.name, avg(grades.grade)
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5