SELECT students.name, grade
FROM groups
JOIN students ON students.group_id = groups.name
JOIN grades ON grades.student_id = students.id
JOIN subjects ON subjects.id = grades.subject_id
WHERE groups.name = '9082'
AND subject_name = 'Music therapist'
AND datetime(timestamp, 'unixepoch') > CURRENT_DATE