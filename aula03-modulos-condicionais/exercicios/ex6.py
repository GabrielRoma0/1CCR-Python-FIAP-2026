"""
- Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações
matemáticas (+, -, *, /)

▪ O programa deve calcular o valor final de acordo com a operação selecionada.

▪ Ou seja, se a entrada for 5, 6 e *, então seu programa dever mostrar 30

"""

n1 = float(input('Digite o primeiro número : '))
caractere = input('Digite um caractere matemático (+, -, *, /) para efetuar a operação entre os números : ')
n2 = float(input('Digite o segundo valor : '))

if caractere == '+':
    print(f'O valor da soma é {n1+n2}')
elif caractere == '-':
    print(f'O valor da subtração é {n1-n2}')
elif caractere == '*':
    print(f'O valor da multiplicação é {n1*n2}')
elif caractere == '/':
    print(f'O valor da divisão é {n1/n2:.2f}')
else:
    print(f'Opção inválida... Tente novamente!')