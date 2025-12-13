# impprtamos el modulo sqlite3
import sqlite3

# conexion a nuestra base de datos
conn = sqlite3.connect("python_avanzado")

# nos permite ejecutar comando en la DB
cursor = conn.cursor()

# creamos una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER
)
""")

# confirmamos
conn.commit()

# insertamos dos registros en la DB
# cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Pablo", 35))
# cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Maria", 25))

# confirmamos
# conn.commit()

# leer os datos en la DB
cursor.execute("SELECT * FROM usuarios")

filas = cursor.fetchall()

print(filas)

for fila in filas:
    print(f"id: {fila[0]}")



# cerrar la conexion
conn.close()
