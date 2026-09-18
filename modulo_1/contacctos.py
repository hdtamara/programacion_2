contactos = {
    "maria":{
        "nombre_completo":"MARIA JOSE HERNANDEZ CARRILLO",
        "telefono":"314567890",
        "direccion":"malambito efectivo"
    },
    "nicolas":{
        "nombre_completo":"NICOLAS DAVID TROCHA SIMANCAS",
        "telefono":"3152895674",
        "direccion":"Rebolo"
    }
}

print(contactos.keys())

for i,key in enumerate(contactos):
    print(i+1,"-",key)
# print(contactos["maria"]['nombre_completo'])