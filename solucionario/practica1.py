mensaje="Hola mundo"

print(mensaje)

nombre = input("Ingresa tu nombre: ")
print(f"Hola, {nombre}")

edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")

numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

numero = int(input("Ingresa un número entero: "))
suma = numero * (numero + 1) // 2
print(f"La suma de los números de 1 a {numero} es: {suma}")