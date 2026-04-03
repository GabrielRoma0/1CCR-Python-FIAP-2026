"""
Faça um programa que receba o ano de nascimento da pessoa e retorne:

▪ Se o voto é obrigatório este ano;
▪ Se o voto é opcional este ano;
▪ Se o voto é proibido este ano.

"""

nasc = int(input('Digite o seu ano de nascimento :'))
ano = int(input('Digite o ano atual :'))
idade = ano - nasc

#NÃO PODEM VOTAR
if idade < 16:
    print('Voto proibido este ano.')

#VOTO OPCIONAL
elif 17 >= idade >= 16:
    print('Voto opcional este ano')
elif idade > 70:
    print('Voto opcional este ano.')

#VOTO OBRIGATÓRIO
else:
    print('Voto obrigatório este ano.')