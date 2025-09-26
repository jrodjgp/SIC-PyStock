import sqlite3
#pense en utilizar sqllite ya que asi es directo en python
# en vez de conectarlo con una base de datos afuera

db_file = 'PyStock.db'

conexion = sqlite3.connect(db_file)
cursor = conexion.cursor()

#primera tabla de producto, 
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id_producto    INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre         TEXT NOT NULL,
    sku            TEXT UNIQUE,
    precio         REAL,
    cantidad_stock INTEGER
)
""")

cursor.execute("SELECT * FROM productos")
todosProductos = cursor.fetchall()

if todosProductos:
    for id_p, nombre, sku, precio, stock in todosProductos:
        print(f"ID: {id_p}")
        print(f"  Nombre: {nombre}")
        print(f"  SKU: {sku}")
        print(f"  Precio: ${precio}")
        print(f"  Stock: {stock} unidades")

#recordar siempre cerrar la conexion
conexion.close()