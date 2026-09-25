def mostrar_bienvenida():
    print("Bienvenido a Programación II")
    print("IUB - Barranquilla")

def saludar(nombre:str):
    print(f"Hola, {nombre}!")

# saludar("Hernan")
# saludar("Valerie")
# saludar("Carlos")

def presentar(nombre:str, edad:int, ciudad:str="Barranquilla"):
    print(f"{nombre}, {edad} años, de {ciudad}")

#presentar("Hernan",31,"Sincelejo") 
#presentar("Angie",25)

def suma(a,b):
    result=a + b
    return result
    #print(a+b)
# suma(2,2)
resultado=suma(5,2)
# print(f"El resultado es {resultado}")

def sumar_listas(listas:list)->float:
    """Suma los numeros de una lista

    Args:
        listas (list): lista numeros

    Returns:
        float: la suma resultante
    """
    sumatoria = 0
    for i in listas:
        sumatoria += i
    return sumatoria

numeros = [2,4,6,8,10]
print(sumar_listas(numeros))

numeros_2 = [5,6,7,8,9]
print(sumar_listas(numeros_2))

numeros_3 = [5,8,9,8,9]
print(sumar_listas(numeros_3))



