"""
▪ Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado
no salário atual:
▪ Salários até R$ 280,00 (incluindo): aumento de 20%.
▪ Salários entre R$ 280,00 e R$ 700,00: aumento de 15%.
▪ Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%.
▪ Salários de R$ 1500,00 em diante: aumento de 5%.
▪ Após o aumento ser realizado, informe na tela:
▪ O salário antes do reajuste.
▪ O percentual de aumento aplicado.
▪ O valor do aumento.
▪ O novo salário, após o aumento.

"""

sal = float(input('Qual é o salário do colaborador : '))

if sal <= 280:
    print(f'O salário com reajuste ficará igual a {1.2*sal}.\nO salário anterior era igual a: {sal}\nO percentual de aumento foi de 20%')
elif 280 < sal < 700:
    print(f'O salário com reajuste ficará igual a {1.15 * sal}\nO salário anterior era igual a: {sal}\nO percentual de aumento foi de 15%')
elif 700 < sal < 1500:
    print(f'O salário com reajuste ficará igual a {1.1 * sal}\nO salário anterior era igual a: {sal}\nO percentual de aumento foi de 10%')
elif sal > 1500:
    print(f'O salário com reajuste ficará igual a {1.05 * sal}\nO salário anterior era igual a: {sal}\nO percentual de aumento foi de 5%')
else:
    print('Valor não realizado!')

    