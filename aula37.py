"""
Operadores de atribuição
=  +=  -=  *=  /=  //=  **=  %=  (retornam a sua operação)
"""

contador = 0

# while contador < 10:
#     contador = contador + 1
#     print(contador)

# print('Acabou')

# contador += 1
# print(contador)

# break e continue = formas de parar o while --> sempre referem-se ao while mais próximo.

while contador <= 100:
    contador += 1  

    if contador == 6:
        print('Não vou mostrar o 6')
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')