# Python-FastApi-project
 FastApi project whith crud operations 

В первую очередь ты должен скачать библиотеки с фала requirements.txt

pip install requirements.txt

в этом фале написанны все нужные библиотеки а точнее
fastapi==0.110.0
sqlalchemy==2.0.29
psycopg2-binary==2.9.9
pydantic==2.6.4
uvicorn==0.29.0


Потом ты должен создать таблици в pg admin
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);


CREATE TABLE recipe_tag (
    recipe_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (recipe_id, tag_id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

Дополнительные файлы проекта
Ниже приведены файлы с кодом, необходимым для реализации проекта FastAPI с операциями CRUD. Каждый файл заключён в тег <xaiArtifact> с уникальным artifact_id.

1. database.py — Конфигурация базы данных
2. models.py — Модели SQLAlchemy
3. schemas.py — Схемы Pydantic
4. crud.py — Операции CRUD
5. main.py — Приложение FastAPI
6. requirements.txt — Зависимости


Установите зависимости:
bash

Копировать
pip install -r requirements.txt
Настройте PostgreSQL:
Создайте базу данных в pgAdmin (например, recipe_db).
Выполните SQL-команды из README.md для создания таблиц.
Настройте database.py: Обновите переменную DATABASE_URL с вашими данными PostgreSQL.
Инициализируйте базу данных:
bash

Копировать
python database.py
Запустите приложение FastAPI:
bash

Копировать
uvicorn main:app --reload
Доступ к API: Откройте браузер и перейдите по адресу http://127.0.0.1:8000/docs, чтобы взаимодействовать с API через Swagger UI.

Следующий шаг это подключить pgadmin в файле database в поле DATABASE_URL = напиши свойё имя пользователя пороль, localhost:5432 и название database



Последние шаги это запустить код в папке database что бы подключить базу даных после этого ты должен окрыть новый терминал и запустить main.py тебе в терменали датут ссылку по это сылке ды должен зайти она будет выгледить как то так "127.0.0.1" после этого ты к ссылке должен написать "/docs" что бы попасть в раздел fastapi что бы использовать "crud operations" добавляешь информацию и она должна сохраняться в твоём базе данных
