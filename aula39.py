# exercicio while - interando strings com while

#       0123456789......
nome = 'Luccas Fernandes'
#      -.......987654321
# tamanhoNome = len(nome)
# print(nome)
# print(tamanhoNome)

indice = 0
nomeConcatenado = ''

while indice < len(nome):
    letra = nome[indice]
    nomeConcatenado += f'*{letra}'
    indice += 1

nomeConcatenado += '*'
print(nomeConcatenado)