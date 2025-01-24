ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]

def mostrar_listado():
    print("Listado de ventas:")
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {'Sí' if venta['promocion'] else 'No'}")

def anadir_producto():
    fecha = input("Ingrese la fecha (dd-mm-yyyy): ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))
    precio = float(input("Ingrese el precio del producto: "))
    promocion = input("¿El producto está en promoción? (s/n): ").lower() == 's'
    ventas.append({"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio": precio, "promocion": promocion})
    print("Producto añadido con éxito.")

def calcular_suma_total():
    suma_total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    print(f"La suma total de las ventas es: {suma_total:.2f}")

def calcular_promedio():
    suma_total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    total_ventas = len(ventas)
    promedio = suma_total / total_ventas if total_ventas > 0 else 0
    print(f"El promedio de ventas es: {promedio:.2f}")

def producto_mas_vendido():
    if not ventas:
        print("No hay productos en la lista de ventas.")
        return
    producto_mas_vendido = max(ventas, key=lambda x: x['cantidad'])
    print(f"El producto con más unidades vendidas es: {producto_mas_vendido['producto']} ({producto_mas_vendido['cantidad']} unidades)")

def mostrar_listado_productos():
    productos = set(venta['producto'] for venta in ventas)
    print("Listado de productos:")
    for producto in productos:
        print(producto)

def ejecutar_opcion(opcion):
    if opcion == "1":
        mostrar_listado()
    elif opcion == "2":
        anadir_producto()
    elif opcion == "3":
        calcular_suma_total()
    elif opcion == "4":
        calcular_promedio()
    elif opcion == "5":
        producto_mas_vendido()
    elif opcion == "6":
        mostrar_listado_productos()
    elif opcion == "7":
        print("Saliendo del programa...")
        return False
    else:
        print("Opción inválida. Intente de nuevo.")
    return True

print("\nMENÚ DE OPCIONES")
print("1. Mostrar el listado de ventas")
print("2. Añadir un producto")
print("3. Calcular la suma total de las ventas")
print("4. Calcular el promedio de ventas")
print("5. Mostrar el producto con más unidades vendidas")
print("6. Mostrar el listado de productos")
print("7. Salir")

opcion = input("\nSeleccione una opción: ")
ejecutar_opcion(opcion)