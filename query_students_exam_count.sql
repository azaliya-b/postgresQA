SELECT s.name, COUNT(e.c_no) AS exam_count
FROM Students s
JOIN Exams e ON s.s_id = e.s_id
GROUP BY s.s_id, s.name;
