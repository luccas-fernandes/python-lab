'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é ímpar
ou par. Caso não digite um número inteiro, informe que não é um número inteiro.
'''

numeroInteiro = input('Digite um número inteiro: ')
if numeroInteiro.isdigit(): 
    numeroInteiro = int(numeroInteiro)
    if numeroInteiro % 2 != 0:
        print('O número escolhido é impar')
    else:
        print('O número escolhido é par')
else: 
    print('Você não digitou um número inteiro.')


