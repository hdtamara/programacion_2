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
        contactos[nombre] = {
            "telefono":telefono,
            "email":email,
            "direccion":direccion
        }    
        print(f"Contacto {nombre} gurdado exitosamente ✅") 
    elif opcion_elegida == 2:
        nombre = input("Ingrese el nombre a buscar: ").lower()
        if nombre in contactos:
            print("="*10)
            print(contactos[nombre])
            print("="*10)
        else:
            print("Contacto no existe")
    elif opcion_elegida == 3:
        nombre = input("Ingrese el nombre del contacto a eliminar: ").lower()
        if nombre in contactos:
            del contactos[nombre]
            print(f"Contacto {nombre} eliminado exitosamente ✅")
        else:
            print(f"Contacto  {nombre} no registrado ❌")
            
    elif opcion_elegida == 4:
        for i,key in enumerate(contactos):
            print(i+1,"-",key)
    elif opcion_elegida == 5:
        print("Hasta la vista Baby")
        break
    else:
        print("Opcion invalida intenta nuevamente")