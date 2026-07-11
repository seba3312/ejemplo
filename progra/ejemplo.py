
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


def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock de Notebook por código")
    print("2. Búsqueda de Notebooks por rango de precio")
    print("3. Actualizar precio de un Notebook")
    print("4. Agregar nuevo Notebook")
    print("5. Eliminar Notebook")
    print("6. Salir del programa")
    print("=====================================")
    opcion = validar_numeros("Seleccione una opción: ")
    if opcion == 1:
menu()
