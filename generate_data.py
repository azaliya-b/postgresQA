from faker import Faker
import psycopg2
import random
import argparse
import os

# Конфигурация через аргументы или переменные окружения
parser = argparse.ArgumentParser()
parser.add_argument('--dbname', default=os.getenv('DB_NAME', 'academy'))
parser.add_argument('--user', default=os.getenv('DB_USER', 'postgres'))
parser.add_argument('--password', default=os.getenv('DB_PASSWORD', 'postgres'))
parser.add_argument('--host', default=os.getenv('DB_HOST', 'localhost'))
parser.add_argument('--port', default=os.getenv('DB_PORT', '5432'))
args = parser.parse_args()

fake = Faker('ru_RU')

try:
    print(f"Подключаюсь к базе с параметрами:")
    print(f"dbname={args.dbname}")
    print(f"user={args.user}")
    print(f"password={args.password}")
    print(f"host={args.host}")
    print(f"port={args.port}")
    
    conn = psycopg2.connect(
        dbname=args.dbname,
        user=args.user,
        password=args.password,
        host=args.host,
        port=args.port
    )
    cur = conn.cursor()

    # Добавление студентов (пример для другой схемы)
    for _ in range(10):
        name = fake.name()
        year = random.randint(2019, 2025)
        # Если структура таблицы отличается:
        cur.execute(
            "INSERT INTO students (name, start_year) VALUES (%s, %s)",
            (name, year)
        )

    # Добавление курсов
    courses = ['Математика', 'Физика', 'Информатика', 'История', 'Экономика']
    for title in courses:
        # Если в таблице courses есть поле hours:
        hours = random.choice([30, 45, 60, 90])
        cur.execute(
            "INSERT INTO courses (title, hours) VALUES (%s, %s)",
            (title, hours)
        )

    # Получение ID студентов и курсов
    cur.execute("SELECT s_id FROM students")
    students = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT c_no FROM courses")
    c_ids = [row[0] for row in cur.fetchall()]

    # Добавление экзаменов
    for student in students:
        # Выбираем случайные уникальные курсы для студента
        for course in random.sample(c_ids, random.randint(1, len(c_ids))):
            score = random.randint(1, 5)  # Оценка от 1 до 5
            cur.execute(
                """INSERT INTO exams (s_id, c_no, score)
                   VALUES (%s, %s, %s)
                   ON CONFLICT DO NOTHING""",
                (student, course, score)
            )

    conn.commit()
    print("Данные успешно сгенерированы!")

except psycopg2.Error as e:
    print(f"Ошибка подключения к БД: {e}")
finally:
    if 'conn' in locals():
        cur.close()
        conn.close()
