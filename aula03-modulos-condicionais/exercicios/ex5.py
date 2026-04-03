"""
Faça um programa que leia 2 valores inteiros (A e B).

- A seguir, o programa deve mostrar uma mensagem "São Múltiplos" ou "Não são Múltiplos", indicando
se os valores lidos são múltiplos entre si.

Dica:
▪ Como que eu sei que 2 números são ou não são múltiplos um do outro?
▪ Conjunto dos Múltiplos de 2 = {2, 4, 6, 8, 10, ...}
▪ Então se observa que os múltiplos de um número são divisíveis por esse número, então o resto dessa
divisão será 0.

"""

val1 = int(input('Digite o valor A :'))
val2 = int(input('Digite o valor A :'))

if val1%val2 == 0:
    print(f'Os valores {val1} e {val2} são múltiplos.')