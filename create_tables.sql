-- Создаем таблицы по схеме
CREATE TABLE Students (
    s_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    start_year INT CHECK (start_year >= 2000 AND start_year <= 2100)
);

CREATE TABLE Courses (
    c_no SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    hours INT CHECK (hours > 0)
);

CREATE TABLE Exams (
    s_id INT,
    c_no INT,
    score NUMERIC(5,2) CHECK (score >= 0 AND score <= 100),
    PRIMARY KEY (s_id, c_no),
    FOREIGN KEY (s_id) REFERENCES Students(s_id) ON DELETE CASCADE,
    FOREIGN KEY (c_no) REFERENCES Courses(c_no) ON DELETE CASCADE
);
