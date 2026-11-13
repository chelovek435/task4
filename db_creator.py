import sqlite3 as sl

fname = 'coffee.sqlite'
with sl.connect(fname) as con:
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS coffee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            variety TEXT NOT NULL,
            roast TEXT NOT NULL,
            type TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            volume REAL NOT NULL
        )
    ''')
    coffee_data = [
        ('Арабика Эфиопия', 'Светлая', 'В зернах', 'Цветочный аромат', 1200,
         250),
        ('Робуста Вьетнам', 'Темная', 'Молотый', 'Крепкий, горьковатый', 800,
         250),
        ('Колумбия Супремо', 'Средняя', 'В зернах', 'Ореховый вкус', 1500, 500)
    ]
    cur.executemany('''
        INSERT INTO
        coffee (variety, roast, type, description, price, volume)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', coffee_data)
    con.commit()
