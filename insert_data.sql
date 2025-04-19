-- Студенты
INSERT INTO Students (name, start_year) VALUES
('Иван Иванов', 2022),
('Мария Смирнова', 2023),
('Петр Кузнецов', 2021);

-- Курсы
INSERT INTO Courses (title, hours) VALUES
('Математика', 60),
('Информатика', 80),
('Физика', 70);

-- Экзамены
INSERT INTO Exams (s_id, c_no, score) VALUES
(1, 1, 85),
(1, 2, 90),
(2, 1, 78);
