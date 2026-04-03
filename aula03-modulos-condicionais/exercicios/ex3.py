#Faça um programa que peça dois números e imprima o maior deles, e informe caso eles sejam iguais.

num1 = float(input('Digite o primeiro número :'))
num2 = float(input('Digite o segundo número :'))

if num1 > num2:
    print(f'O primeiro número ({num1}) é maior.')
elif num2 > num1:
    print(f'O segundo número ({num2}) é maior.')
else:
    print(f'Os dois números são iguais a ({num1})')