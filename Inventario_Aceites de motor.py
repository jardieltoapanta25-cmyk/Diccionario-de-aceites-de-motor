#Ejercicio de colecciones 
#Reguistro de aceites y sus rangos de viscosidad

inventario = {
    "Gulf 10W-30": 5,
    "Shell 20W-50": 7,
    "Mobil 15W-40": 6,
    "Castrol 5W-25": 8
}

def mostrar_inventario():
    print("\n--- ACEITES EN BODEGA ---")
    for aceite, cantidad in inventario.items():
        print(f"{aceite}: {cantidad} unidades")

def registrar_entrada():
    aceite = input("Nombre del aceite que ingresa: ").title()
    cantidad = int(input("Cantidad que ingresa: "))
    if aceite in inventario:
        inventario[aceite] = inventario[aceite] + cantidad
    else:
        inventario[aceite] = cantidad
    print(f"Entrada registrada: +{cantidad} de {aceite}")

def registrar_salida():
    aceite = input("Nombre del aceite que sale: ").title()
    cantidad = int(input("Cantidad que sale: "))
    if aceite in inventario and inventario[aceite] >= cantidad:
        inventario[aceite] = inventario[aceite] - cantidad
        print(f"Salida registrada: -{cantidad} de {aceite}")
    else:
        print("Error: No hay suficiente stock o el aceite no existe.")

def buscar_aceite():
    aceite = input("Nombre del aceite a buscar: ").title()
    if aceite in inventario:
        print(f"{aceite}: {inventario[aceite]} unidades en bodega")
    else:
        print("Ese aceite no está en el inventario.")

while True:
    print("\n===== INVENTARIO DE ACEITES DE MOTOR =====")
    print("1. Ver inventario")
    print("2. Registrar entrada")
    print("3. Registrar salida")
    print("4. Buscar aceite")
    print("5. Salir")
    opcion = input("Elija una opción: ")
    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        registrar_entrada()
    elif opcion == "3":
        registrar_salida()
    elif opcion == "4":
        buscar_aceite()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
