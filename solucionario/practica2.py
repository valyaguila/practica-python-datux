# Inicializamos una lista para almacenar los productos y sus ventas
productos = []  # Lista de diccionarios con nombre y unidades vendidas

def mostrar_menu():
    print("\nMENÚ INTERACTIVO DE VENTAS")
    print("1. Mostrar listado de ventas")
    print("2. Añadir un producto")
    print("3. Calcular suma total de ventas")
    print("4. Calcular promedio de ventas")
    print("5. Mostrar producto con más unidades vendidas")
    print("6. Mostrar listado de productos")
    print("7. Salir")

def mostrar_ventas():
    if not productos:
        print("\nNo hay ventas registradas.")
    else:
        print("\n=== LISTADO DE VENTAS ===")
        for producto in productos:
            print(f"Producto: {producto['nombre']}, Unidades vendidas: {producto['unidades']}")

def añadir_producto():
    nombre = input("\nIngrese el nombre del producto: ")
    while True:
        try:
            unidades = int(input("Ingrese las unidades vendidas: "))
            if unidades >= 0:
                break
            print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    productos.append({'nombre': nombre, 'unidades': unidades})
    print("Producto añadido exitosamente.")

def calcular_total_ventas():
    total = sum(producto['unidades'] for producto in productos)
    print(f"\nTotal de unidades vendidas: {total}")
    return total

def calcular_promedio():
    if not productos:
        print("\nNo hay ventas para calcular el promedio.")
        return
    total = calcular_total_ventas()
    promedio = total / len(productos)
    print(f"Promedio de ventas: {promedio:.2f}")

def producto_mas_vendido():
    if not productos:
        print("\nNo hay productos registrados.")
        return
    
    max_producto = max(productos, key=lambda x: x['unidades'])
    print(f"\nProducto más vendido: {max_producto['nombre']} con {max_producto['unidades']} unidades")

def mostrar_productos():
    if not productos:
        print("\nNo hay productos registrados.")
    else:
        print("\n=== LISTADO DE PRODUCTOS ===")
        for i, producto in enumerate(productos, 1):
            print(f"{i}. {producto['nombre']}")

# Mostrar el menú una sola vez y ejecutar la opción seleccionada
mostrar_menu()
opcion = input("\nSeleccione una opción (1-7): ")

if opcion == '1':
    mostrar_ventas()
elif opcion == '2':
    añadir_producto()
elif opcion == '3':
    calcular_total_ventas()
elif opcion == '4':
    calcular_promedio()
elif opcion == '5':
    producto_mas_vendido()
elif opcion == '6':
    mostrar_productos()
elif opcion == '7':
    print("\n¡Gracias por usar el sistema!")
else:
    print("\nOpción no válida.")