import sqlite3 as sql


def sql_connector():
    con = sql.connect("flask_site.db")
    cur = con.cursor()
    return con, cur


def create_tables():
    con, cur = sql_connector()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_img VARCHAR(200),
                rent_price INTEGER
                )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS blog(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR(100),
                    description TEXT,
                    image VARCHAR(200),
                    date TIMESTAMP
                    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS cars(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(100),
                    description TEXT
                    )""")


def get_cars():
    con, cur = sql_connector()

    cars = cur.execute("SELECT * FROM cars").fetchall()
    return cars


def get_blogs():
    con, cur = sql_connector()

    blog = cur.execute("SELECT * FROM blog").fetchall()
    return blog
