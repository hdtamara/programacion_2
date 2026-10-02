def validar_contactos(contactos:dict,nombre:str):
    return nombre in contactos

def formatear_contacto(nombre,contacto:dict):
    return f"""
    {"="*15}
    Nombre: {nombre}
    Telefono: {contacto['telefono']}
    Email: {contacto['email']}
    Dirección: {contacto['direccion']}
    {"="*15}
"""

def buscar_contacto(contactos:dict,nombre):
    if validar_contactos(contactos,nombre):
        print(formatear_contacto(nombre,contactos[nombre]))
    else:
        print("Contacto no existe")