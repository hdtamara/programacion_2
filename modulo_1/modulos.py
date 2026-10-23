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

def buscar_contacto(contactos:dict,nombre:str):
    if validar_contactos(contactos,nombre):
        print(formatear_contacto(nombre,contactos[nombre]))
    else:
        print("Contacto no existe")

def eliminar_contacto(contactos:dict,nombre:str):
    if validar_contactos(contactos,nombre):
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado exitosamente ✅")
    else:
        print(f"Contacto  {nombre} no registrado ❌")

def mostrar_contactos(contactos:dict):
    for i,key in enumerate(contactos):
        print(i+1,"-",key)

def guardar_contacto(contactos:dict,nombre,telefono,email,direccion):
    contactos[nombre] = {
    "telefono":telefono,
    "email":email,
    "direccion":direccion
    }    
    print(f"Contacto {nombre} gurdado exitosamente ✅")
    

precios = {
    "yuca":1500,
    "arroz":2500
}

pedidos = {
"arroz":5,
"yuca":5
}

total = 0
contador = 0
for key,value in pedidos.items():
    subtotal = precios[key]*value
    total += subtotal
    contador += value
print(total)
print(contador)
    
    