# diccionario = {}
# diccionario["nombre"] = "Hernán"
# diccionario["apellido"] = "Támara"
# print(diccionario)
# print(diccionario["nombre"])
# diccionario["nombre"] = "Hernando"
# print(diccionario)
# del diccionario["apellido"]
# print(diccionario)
# # eliminado = diccionario.pop("nombre")
# # print(eliminado)
# # print(diccionario)
# #mezclar diccionarios
# diccionario_2 = {
#     "edad":31,
#     "telefono":"3004568765"
# }
# diccionario.update(diccionario_2)
# print(diccionario)

contactos = {
    "Hernan":{
        "apellido":"Tamara",
        "telefono":"3004568765"
    },
    "Stefanny":{
        "apellido":"Cantillo",
        "telefono": "3057684532"
    }
}

print(contactos["Hernan"]["telefono"])
# contactos['Hernan']="Támara"
print(contactos)
contactos["Hernan"]["apellido"]="Támara"