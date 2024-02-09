SELECT students.name
FROM groups
JOIN students ON students.group_id = groups.name
WHERE groups.name = '9082'