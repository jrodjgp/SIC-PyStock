import sqlite3

db_file = 'PyStock.db'

# 1. Conectamos a la base de datos
conexion = sqlite3.connect(db_file)
cursor = conexion.cursor()

# 2. Creamos la tabla (SOLO SI NO EXISTE YA)
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    nombre TEXT,
    edad INTEGER
)
""")

# 3. Insertamos algunos datos para asegurarnos de que no esté vacía
# (Puedes comentar estas líneas después de la primera ejecución)
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Carlos", 40))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Beatriz", 25))

# Guardamos las inserciones
conexion.commit()

# 4. Seleccionamos y mostramos todos los datos
print("Recuperando todos los datos de la tabla 'usuarios'...")
cursor.execute("SELECT * FROM usuarios")
todos_los_usuarios = cursor.fetchall()

print("--- Usuarios Encontrados ---")
if todos_los_usuarios:
    for usuario in todos_los_usuarios:
        print(f"Nombre: {usuario[0]}, Edad: {usuario[1]}")
else:
    print("No se encontraron usuarios.")
print("--------------------------")


# 5. Cerramos la conexión
conexion.close()