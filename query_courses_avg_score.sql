SELECT c.title, AVG(e.score) AS avg_score
FROM Courses c
JOIN Exams e ON c.c_no = e.c_no
GROUP BY c.c_no, c.title
ORDER BY avg_score DESC;
