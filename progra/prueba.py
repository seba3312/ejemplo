lista_tareas = []


def validar_numeros(mensaje:str)->int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor == 0:
                print("El valor no puede ser cero.")
            elif valor < 0:
                print("No se pueden ingresar numeros negativos.")
            else:
                return valor
        except Exception:
            print("Solo se pueden ingresar numeros. ")

def validar_nombre(mensaje:str)->str:
    while True:
        nombre = input(mensaje)
        if len(nombre) == 0:
            print("El nombre no puede estar vacio.")
        elif len(nombre) < 3:
            print("El nombre no debe contener menos de 3 caracteres.")
        else:
            return nombre
        
def agregar_tarea(idTarea:int,NombreTarea:str,ResponsableTarea:str):
    diccionario = {
        "id_tarea":idTarea,
        "nombre_tarea":NombreTarea,
        "responsable_tarea":ResponsableTarea,
        "estado_tarea":"Pendiente"
    }
    lista_tareas.append(diccionario)
    print("Tarea agregada correctamente.")
def cortafuegos():
    if diccionario == None:
        print("No se encontró la tarea.")

def buscar_tarea(idTarea:int = None, nombreTarea:str = None)->int | None:
    for posicion, tarea in enumerate(lista_tareas):
        if idTarea is not None and tarea.get("id_tarea") == idTarea:
            return posicion
        elif nombreTarea is not None and tarea.get("nombre_tarea").lower() == nombreTarea:
            return posicion
    return None
def eliminar_tarea(posicion:int):
    lista_tareas.pop(posicion)
    print("Tarea eliminada.")

def actualizar_tarea(posicion:int,estado_tarea:str):
    if estado_tarea.capitalize() == "Pendiente" or estado_tarea.capitalize() == "En proceso" or estado_tarea.capitalize() == "Completada":
        lista_tareas[posicion]["estado_tarea"] = estado_tarea
        print("Tarea se actualizo correctamente.")
    else:
        print("No existe el estado de la tarea que se acaba de ingresar.")
def mostrar_tareas():
    if len(lista_tareas) == 0:
        print("No hay tareas registradas.")
    else:
        for tarea in lista_tareas:
            print(f" [ID TAREA]: {tarea.get('id_tarea')} - [NOMBRE TAREA]: {tarea['nombre_tarea']} - [RESPONSABLE]: {tarea['responsable_tarea']} - [ESTADO]: {tarea['estado_tarea']}")

def menu():
    while True:
        print("1. Agregar tarea")
        print("2. Buscar tarea")
        print("3. Eliminar tarea")
        print("4. Actualizar estado de tarea")
        print("5. Mostrar tareas")
        print("6. Salir")
        opcion = validar_numeros("Ingrese una opcion: ")
        if opcion == 1:
            idTarea = validar_numeros("Ingrese el id de la tarea: ")
            nombreTarea = validar_nombre("Ingrese el nombre de la tarea: ")
            responsableTarea = validar_nombre("Ingrese el nombre del responsable: ")
            agregar_tarea(idTarea, nombreTarea, responsableTarea)
        elif opcion == 2:
            buscar_tarea("Ingrese la opción de búsqueda (Id/Nombre): ")
        elif opcion == 3:
            posicion = validar_numeros("Ingrese la posición de la tarea a eliminar: ")
            eliminar_tarea(posicion)
        elif opcion == 4:
            tarea = input('¿Como desea buscar la tarea a actualizar? (Id/Nombre): ')
            if tarea == "Id":
                id_tarea = validar_numeros("Ingrese el id de la tarea a modificar: ")
                tarea_encontrada = buscar_tarea(idTarea=id_tarea)
            elif tarea == "Nombre":
                nombre_tarea = validar_nombre("Ingrese el nombre de la tarea a modificar: ")
                tarea_encontrada = buscar_tarea(nombreTarea=nombre_tarea)
            else:
                print("Opción no válida.")
                continue

            if tarea_encontrada is None:
                print("No se encontró la tarea.")
            else:
                estado_tarea = validar_nombre("Ingrese nuevo estado de la tarea: ")
                actualizar_tarea(tarea_encontrada, estado_tarea)
        elif opcion == 5:
            mostrar_tareas()
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Por favor, ingrese una opcion del 1 al 6.")
menu()