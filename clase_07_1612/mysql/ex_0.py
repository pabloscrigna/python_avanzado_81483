import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="python123",
    database="eduit"
)

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nombre VARCHAR(50) NOT NULL,
#     edad INT
# )
# """)
# conn.commit()

# sql_insert = "INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)"
# cursor.execute(sql_insert, ("Pablo", 35))
# cursor.execute(sql_insert, ("Ana", 28))
# conn.commit()

cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()

print("\nListado de usuarios:")
for row in rows:
    print(row)

cursor.execute("""
UPDATE usuarios
SET edad = %s
WHERE nombre = %s
""", (40, "Pablo"))
conn.commit()

cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()

print("\nListado de usuarios:")
for row in rows:
    print(row)

conn.close()