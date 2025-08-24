# Скрипт для исправления плохих оценок, удаления замечаний и добавление похвал!

Скрипт позволяет исправлять оценки 2 и 3, на 5. А тк же удаляет замечания и добавляет похвалу ученику в электронный дневник.

## Установка

1. Создайте и активируйте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # для Linux/MacOS
venv\Scripts\activate     # для Windows
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте файл .env:

Создайте файл ```.env``` в той же директории что и скрипт ```script.py```

```
DEBUG=True
SECRET_KEY=ваш_секретный_ключ
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_NAME=schoolbase.sqlite3
```
- ```DEBUG=True``` - включение отладочного режима (True/False)
- ```SECRET_KEY``` - ваш_секретный_ключ
- ```ALLOWED_HOSTS``` - разрешенные хосты через запятую
- ```DATABASE_NAME``` - путь до базы данных


## Как запустит:

Параметры по умолчанию имя ученика None, урок "Математика", похвала "Молодец!"

Для запуска скрипта необходимо перейти в директорию cd (путь к директории)

1. Запустить скрипт manage.py в shell:
   Выполните команду ```python manage.pi shell```

   Выполните в самом shell:
   ```
   from script import fix_student
   fix_student("Юдин Степан Филатович")
   ```
   
   Пример выполнения
   
   <img width="389" height="119" alt="image" src="https://github.com/user-attachments/assets/7c5682e6-0e4a-4ea6-b277-6e04320443f0" />

   
   Ошибка в ФИО ученика
   
   <img width="324" height="68" alt="image" src="https://github.com/user-attachments/assets/6f8390e9-6c5a-4881-bfe8-858880962e23" />


2. Для внесения похвалы других предметов.
   ```
   fix_student("Фролов Иван", subject_title="Литература", commendation_text="Отличная работа на уроке!")
   ```


   
   
