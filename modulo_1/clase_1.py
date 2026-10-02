import modulos
from modulos import buscar_contacto

nombres = []
telefonos = []
emails = []
direcciones = []

contactos= {}

while True:
    menu = """
    
    ### ELIGE UNA OPCION ###
    
    1. Agregar un contacto.
    2. Busca un contacto.
    3. Eliminar un contacto.
    4. Ver Contactos
    5. Salir
    """
    
    opcion_elegida = int(input(menu))
    
    if opcion_elegida == 1:
        nombre = input("Ingrese el nombre: ")
        nombre = nombre.lower()
        telefono = input("Ingrese el telefono: ")
        email = input("Ingrese su email: ")
        direccion = input("Ingrese su dirección: ")
        modulos.guardar_contacto(contactos,nombre,telefono,email,direccion)
    elif opcion_elegida == 2:
        nombre = input("Ingrese el nombre a buscar: ").lower()
        buscar_contacto(contactos,nombre)
    elif opcion_elegida == 3:
        nombre = input("Ingrese el nombre del contacto a eliminar: ").lower()
        modulos.eliminar_contacto(contactos,nombre)
    elif opcion_elegida == 4:
        modulos.mostrar_contactos(contactos)
    elif opcion_elegida == 5:
        print("Hasta la vista Baby")
        break
    else:
        print("Opcion invalida intenta nuevamente")