
from faker import Faker
import psycopg2
import random

fake = Faker('ru_RU')  # Русская локализация

conn = psycopg2.connect(
    dbname="academy",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Добавим студентов
for _ in range(10):
    name = fake.name()
    year = random.randint(2019, 2025)
    cur.execute("INSERT INTO Students (name, start_year) VALUES (%s, %s)", (name, year))

# Русские курсы
courses = ['Математика', 'Физика', 'Информатика', 'История', 'Экономика']
for title in courses:
    hours = random.choice([30, 45, 60, 90])
    cur.execute("INSERT INTO Courses (title, hours) VALUES (%s, %s)", (title, hours))

# Добавим экзамены
cur.execute("SELECT s_id FROM Students")
students = [row[0] for row in cur.fetchall()]

cur.execute("SELECT c_no FROM Courses")
course_ids = [row[0] for row in cur.fetchall()]

for student in students:
    for course in random.sample(course_ids, random.randint(1, len(course_ids))):
        score = round(random.uniform(50, 100), 2)
        cur.execute("""
            INSERT INTO Exams (s_id, c_no, score)
            VALUES (%s, %s, %s)
            ON CONFLICT DO NOTHING
        """, (student, course, score))

conn.commit()
cur.close()
conn.close()


