class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  

    def asignar_horario(self, hora):
        if hora in self.horarios:
            return False  
        self.horarios.append(hora)
        return True

class Buses:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = [] 
        self.conductores_asignados = [] 

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario):
        if horario in self.horarios:
            return False 
        self.horarios.append(horario)
        return True

    def asignar_conductor(self, conductor, horario):
        if horario in conductor.horarios:
            return False

        if horario not in self.horarios:
            return False

        conductor.asignar_horario(horario)
        self.conductores_asignados.append((conductor, horario))
        return True

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, id_bus):
        self.buses.append(Buses(id_bus))

    def agregar_conductor(self, nombre):
        self.conductores.append(Conductor(nombre))

    def buscar_bus(self, id_bus):
        for bus in self.buses:
            if bus.id_bus == id_bus:
                return bus
        return None

    def buscar_conductor(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        return None

# Programa principal
admin = Admin()

def menu():
    while True:
        print("\n--- Gestión de Tickets de Buses ---")
        print("1. Agregar Bus")
        print("2. Agregar Ruta a Bus")
        print("3. Registrar Horario a Bus")
        print("4. Agregar Conductor")
        print("5. Agregar Horario a Conductor")
        print("6. Asignar Bus a Conductor")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_bus = input("Ingrese el ID del bus: ")
            admin.agregar_bus(id_bus)
            print(f"Bus {id_bus} agregado correctamente.")

        elif opcion == "2":
            id_bus = input("Ingrese el ID del bus: ")
            bus = admin.buscar_bus(id_bus)
            if bus:
                ruta = input("Ingrese la ruta del bus: ")
                bus.agregar_ruta(ruta)
                print(f"Ruta '{ruta}' agregada al bus {id_bus}.")
            else:
                print("Bus no encontrado.")

        elif opcion == "3":
            id_bus = input("Ingrese el ID del bus: ")
            bus = admin.buscar_bus(id_bus)
            if bus:
                horario = input("Ingrese el horario a registrar (formato HH:MM): ")
                if bus.registrar_horario(horario):
                    print(f"Horario {horario} registrado en el bus {id_bus}.")
                else:
                    print("El horario ya está registrado.")
            else:
                print("Bus no encontrado.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del conductor: ")
            admin.agregar_conductor(nombre)
            print(f"Conductor {nombre} agregado correctamente.")

        elif opcion == "5":
            nombre = input("Ingrese el nombre del conductor: ")
            conductor = admin.buscar_conductor(nombre)
            if conductor:
                horario = input("Ingrese el horario a asignar (formato HH:MM): ")
                if conductor.asignar_horario(horario):
                    print(f"Horario {horario} asignado al conductor {nombre}.")
                else:
                    print("El horario ya está asignado a este conductor.")
            else:
                print("Conductor no encontrado.")

        elif opcion == "6":
            id_bus = input("Ingrese el ID del bus: ")
            bus = admin.buscar_bus(id_bus)
            if bus:
                nombre = input("Ingrese el nombre del conductor: ")
                conductor = admin.buscar_conductor(nombre)
                if conductor:
                    horario = input("Ingrese el horario (formato HH:MM): ")
                    if bus.asignar_conductor(conductor, horario):
                        print(f"Conductor {nombre} asignado al bus {id_bus} en el horario {horario}.")
                    else:
                        print("No se pudo asignar el conductor. Verifique el horario o conflictos.")
                else:
                    print("Conductor no encontrado.")
            else:
                print("Bus no encontrado.")

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

        input("Presione Enter para continuar...")

menu()
