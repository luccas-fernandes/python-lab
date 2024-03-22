"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a 
a saudação apropriada. Ex: Boa tarde 12:03, bom dia 0:11
"""
horaLocal = input('Digite a hora atual:')

horaLocal_2 = int(horaLocal[:2])

if horaLocal_2 > 00 and horaLocal_2 < 12:
    print(f'Bom dia,', horaLocal)

elif horaLocal_2 >= 12 and horaLocal_2 < 18:
    print(f'Boa tarde,', horaLocal)

elif horaLocal_2 >= 18 and horaLocal_2 < 24:
    print(f'Boa noite,', horaLocal)

else:
    print(f'Você não digitou o formato correto.')
   
   
