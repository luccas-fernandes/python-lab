"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva
Seu nome é curto; se tiver entre 5 e 6 letras, escreva "Seu nome é médio"; maior que 6 escreva 
"Seu nome é muito grande".

"""

nomeDoUsuario = input('Digite seu nome: ')
contagemDeCaracteres = len(nomeDoUsuario)

if contagemDeCaracteres <= 4:
    print(f'Seu nome é curto.')

elif contagemDeCaracteres > 4 and contagemDeCaracteres <=6:
    print(f'Seu nome é médio.')

else:
    print(f'Seu nome é grande.')
