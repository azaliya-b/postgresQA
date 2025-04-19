SELECT s.*
FROM Students s
LEFT JOIN Exams e ON s.s_id = e.s_id
WHERE e.s_id IS NULL;
