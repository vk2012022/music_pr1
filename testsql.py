import sqlite3

# Открыть базу данных по указанному пути
db_path = r'C:\Users\vk201\Downloads\db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Выполнить SQL-запрос для получения содержимого таблицы
table_name = 'music_foto_musicpiece'  # Укажите имя таблицы
cursor.execute(f"SELECT * FROM {table_name};")

# Получить имена столбцов
columns = [description[0] for description in cursor.description]

# Вывести имена столбцов
print(f"Содержимое таблицы {table_name}:")
print(columns)

# Вывести строки таблицы
rows = cursor.fetchall()
for row in rows:
    print(row)

# Закрыть соединение с базой данных
conn.close()
