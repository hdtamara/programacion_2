yo = {"nombre": "hernan", "edad": 18, "es_estudiante": False}

yo_lista = ["hernan", 18, False]
print(yo_lista[0])
print(yo["nombre"])

# Modificar un elemento
yo_lista[0] = "Hernán Támara"
print(yo_lista)
yo["nombre"] = "Hernán Támara"
print(yo)
# Agregar un elemento
yo_lista.append("cra 45 #54-46")  # -->Lista
yo["direccion"] = "cra 45 #54-46"
yo["telefono"] = "+57 3040001222"

#Update
yo_2 = {"rh": "o+", "profesion": "Cientifico de datos"}
yo.update(yo_2)
print(yo)

eliminado_1 = yo.pop("profesion")
eliminado_2 = yo.pop("rh")
print(eliminado_1)
print("="*50)
print(yo)
