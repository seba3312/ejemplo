Notebooks = {
    'PC1': ['Asus Rog Zephyrus', '16gb ram ddr5', '1tb disco', 'NVIDIA', 'rtx 4060', 14],
    'PC2': ['Lenovo Legion 5', '16gb ram ddr4', '512gb disco', 'NVIDIA', 'rtx 3060', 15.6],
    'PC3': ['Hp Victus', '8gb ram ddr4', '256gb disco', 'NVIDIA', 'rtx 3050', 15.6],
    'PC4': ['Acer Nitro 5', '16gb ram ddr4', '1tb disco', 'NVIDIA', 'rtx 3050ti', 14],
    'PC5': ['Asus Tuf Gaming', '16gb ram ddr4', '512gb disco', 'NVIDIA', 'rtx 3050ti', 15.6],
    'PC6': ['Asus Rog Strix', '32gb ram ddr5', '1tb disco', 'NVIDIA', 'rtx 4070', 15.6],
}

bodega = {
    'PC1': [1899990, 8],
    'PC2': [699990, 15],
    'PC3': [599990, 12],
    'PC4': [599990, 6],
    'PC5': [699990, 10],
    'PC6': [1499990, 3],
}

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion < 1 or opcion > 6:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")
            else:
                return opcion
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def validar_nombre(mensaje:str)->str:
    while True:
        nombre = input(mensaje)
        if len(nombre) == 0:
            print("El nombre no puede estar vacio.")
        elif " " in nombre:
            print("El nombre no debe contener espacios.")
        else:
            return nombre
def validar_numeros(mensaje:str)->int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor == 0:
                print("El valor no puede ser cero.")
            elif valor < 0:
                print("No se pueden ingresar numeros negativos.")
            elif " " in str(valor):
                print("El valor no debe contener espacios.")
            else:
                return valor
        except Exception:
            print("Solo se pueden ingresar numeros enteros. ")

def detalle_notebook(codigo):
    if codigo in Notebooks and codigo in bodega:
        print(f"Modelo: {Notebooks[codigo][0]}")
        print(f"Memoria RAM: {Notebooks[codigo][1]}")
        print(f"Memoria ROM: {Notebooks[codigo][2]}")
        print(f"Tarjeta de video: {Notebooks[codigo][3]} {Notebooks[codigo][4]}")
        print(f"Tamaño de pantalla: {Notebooks[codigo][5]} pulgadas")
        print(f"Precio: ${bodega[codigo][0]}")
        print(f"Stock disponible: {bodega[codigo][1]} unidades")
    else:
        print("No se encontró la notebook con el código ingresado.")
    
def buscar_precio(precio_min, precio_max, bodega, Notebooks):
    encontrados = []
    for codigo, (precio, stock) in bodega.items():
        if precio_min <= precio <= precio_max:
            encontrados.append(f" Código: {codigo}, Modelo: {Notebooks[codigo][0]}, Precio: ${precio}, Stock: {stock}")
    return encontrados
def menu():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Stock de Notebook por código")
        print("2. Búsqueda de Notebooks por rango de precio")
        print("3. Actualizar precio de un Notebook")
        print("4. Agregar nuevo Notebook")
        print("5. Eliminar Notebook")
        print("6. Salir del programa")
        print("=====================================")
        opcion = leer_opcion()
        if opcion == 1:
            codigo = validar_nombre("Ingrese el código de la notebook: ")
            detalle_notebook(codigo)
        elif opcion == 2:
            while True:
                try:
                    precio_min = float(input("Ingrese el precio mínimo: "))
                    precio_max = float(input("Ingrese el precio máximo: "))
                    if precio_min > precio_max:
                        print("El precio mínimo no puede ser mayor que el precio máximo.")
                        continue
                    elif precio_min < 0 or precio_max < 0:
                        print("El precio no puede ser negativo.")
                        continue
                    else:
                        encontrados = buscar_precio(precio_min, precio_max, bodega, Notebooks)
                        if encontrados:
                            for notebook in encontrados:
                                print(notebook)
                            break
                        else:
                            print("No se encontraron notebooks en el rango de precio especificado.")
                            break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
        

menu()