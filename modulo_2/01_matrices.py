# Matriz
# matriz = [[1,2,3],
#           [4,5,6]]
# matriz[1][2]=9
# print(matriz[0][1])
# print(matriz)

#Vector 
vector = [1,2,3,4,5]
v_mult = [x*2 for x in vector]
print(v_mult)

matriz_1 = [[1,2,3],
          [4,5,6]]

matriz_2 = [[1,2,3],
          [4,5,6]]

matriz_resultado = []

for m1,m2 in zip(matriz_1,matriz_2):
    print(m1)
    print(m2)
    resultado = []
    for x1,x2 in zip(m1,m2):
        print(x1+x2)
        resultado.append(x1+x2)
    matriz_resultado.append(resultado)

print(matriz_resultado)