# **Тестовое задание на позицию стажера QA в Postgres Pro**

# Задание по теории тестирования

Отчет по тестированию интернет-магазина представлен в отдельном документе: Create QA_Strategy_PostgresPro.md.  
В документе описаны:
- Этапы тестирования (альфа-версия, бета-тестирование, релиз, поддержка)
- Виды тестирования (функциональное, интеграционное, нагрузочное и др.)
- Используемые метрики (покрытие требований, дефекты на этапе и т.д.)
- Управление рисками и оценка трудоемкости
- Применение пирамиды тестирования и тест-дизайна

---

# Задание по основам баз данных
## Описание

Проект демонстрирует работу с базой данных студентов, курсов и экзаменов по схеме, представленной в задании. Реализация — на **PostgreSQL**, запуск возможен как нативно, так и через Docker.

---

## 📦 Установка PostgreSQL через Docker

1. Убедитесь, что установлен и работает [Docker Desktop](https://www.docker.com/products/docker-desktop/).
.

🔧 Шаг 1: Запуск контейнера PostgreSQL
Выполните в терминале:

```bash
docker run --name academy-postgres -e POSTGRES_PASSWORD=ваш_пароль -e POSTGRES_USER=имя_пользователя -e POSTGRES_DB=academy -p 5432:5432 -d postgres
```

📌 После запуска база данных academy будет готова к использованию, порт 5432 проброшен, логин/пароль: postgres.

📁 Шаг 2: Клонирование репозитория
Склонируйте репозиторий с заданиями:

```bash
git clone https://github.com/azaliya-b/postgresQA.git
cd postgresQA
```

📂 Шаг 3: Копирование SQL-скриптов в контейнер
Копируйте все нужные скрипты в контейнер. Например:

```bash
docker cp schema.sql academy-postgres:/create_tables.sql
docker cp insert_data.sql academy-postgres:/insert_data.sql
docker cp query_students_no_exams.sql academy-postgres:/query_students_no_exams.sql
docker cp query_students_exam_count.sql academy-postgres:/query_students_exam_count.sql
docker cp query_courses_avg_score.sql academy-postgres:/query_courses_avg_score.sql
```
💻 Шаг 4: Запуск SQL-скриптов в контейнере
Подключитесь к PostgreSQL внутри контейнера:

```bash
docker exec -it academy-postgres psql -U postgres -d academy
```
Затем по очереди выполните скрипты:

```sql
\i schema.sql
\i insert_data.sql
\i query_students_no_exams.sql
\i query_students_exam_count.sql
\i query_courses_avg_score.sql
```
Выход из psql:

```sql
\q
```
Чтобы заполнить таблицы произвольными данными(с помощью generate_data.py) выполнить:

```sql
pip install faker psycopg2-binary

python generate_data.py --dbname=academy --user=имя_пользователя --password=ваш_пароль --host=localhost
```

🧼 Остановка и удаление контейнера
Остановить PostgreSQL:

```bash
docker stop academy-postgres
Удалить контейнер:
```

```bash
docker rm academy-postgres
```

📂 Структура проекта

```bash
academy-db/
├── Create QA_Strategy_PostgresPro.md    -- Задание по теории тестирования
├── create_tables.sql                    -- Скрипт создания таблиц
├── insert_data.sql                      -- Примеры вставки данных
├── query_students_no_exams.sql          -- SQL-запрос, который возвращает всех студентов, которые еще не сдали ни одного экзамена.
├── query_students_exam_count.sql        -- SQL-запрос, , который возвращает список студентов и количество сданных им экзаменов. Только для студентов, у которых есть сданные экзамены.
├── query_courses_avg_score.sql          -- SQL-запрос, который возвращает список курсов со средним баллом по экзамену
├── generate_data.py                     -- Скрипт генерации данных
└── README.md                            -- Описание проекта (этот файл)
```
