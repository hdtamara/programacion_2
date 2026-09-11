nombres = []
telefonos = []
emails = []
direcciones = []

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
        nombres.append(nombre)
        telefonos.append(telefono)
        emails.append(email)
        direcciones.append(direccion)
        print(f"Contacto {nombre} gurdado exitosamente ✅") 
    elif opcion_elegida == 2:
        nombre = input("Ingrese el nombre a buscar: ")
        if nombre in nombres:
            indice = nombres.index(nombre.lower())
            print("="*10)
            print(f"Nombre: {nombres[indice]}")
            print(f"Telefono: {telefonos[indice]}")
            print(f"Email: {emails[indice]}")
            print(f"Dirección: {direcciones[indice]}")
            print("="*10)
            
        else:
            print("Contacto no existe")
    elif opcion_elegida == 3:
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre in nombres:
            indice = nombres.index(nombre.lower())
            nombres.pop(indice)
            telefonos.pop(indice)
            emails.pop(indice)
            direcciones.pop(indice)
            print(f"Contacto {nombre} eliminado exitosamente ✅")
            
    elif opcion_elegida == 4:
        for nombre,telefono,email,direccion in zip(nombres,telefonos,emails,direcciones):
            print(f"Nombre: {nombre}")
            print(f"Telefono: {telefono}")
            print(f"Email: {email}")
            print(f"Dirección: {direccion}")
            print("="*10)
    elif opcion_elegida == 5:
        print("Hasta la vista Baby")
        break
    else:
        print("Opcion invalida intenta nuevamente")