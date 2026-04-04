"""
▪ Faça um programa que leia 3 valores que representam os lados de um triângulo A, B e C e ordene-os
em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o
tipo de triângulo que estes três lados formam, com base nos seguintes casos:
▪ Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
▪ Se A² = B² + C² , apresente a mensagem: TRIANGULO RETANGULO;
▪ Se A² > B² + C² , apresente a mensagem: TRIANGULO OBTUSANGULO;
▪ Se A² < B² + C² , apresente a mensagem: TRIANGULO ACUTANGULO;
▪ Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
▪ Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES;

"""

lado_a = float(input('Digite o lado (A) do triângulo: '))
lado_b = float(input('Digite o lado (B) do triângulo: '))
lado_c = float(input('Digite o lado (C) do triângulo: '))

if lado_a**2 == lado_b**2 + lado_c**2:
    print('Triângulo retângulo! ')
elif lado_a**2 > lado_b**2 + lado_c**2:
    print('Triângulo obtusângulo! ')
elif lado_a**2 < lado_b**2 + lado_c**2:
    print('Triângulo acutângulo! ')
    if lado_a == lado_b == lado_c:
        print('Triângulo equilátero! ')
    elif lado_b == lado_c != lado_a:
        print('Triângulo isósceles! ')
    elif lado_a == lado_c != lado_b:
        print('Triângulo isósceles! ')
    elif lado_a == lado_b != lado_c:
        print('Triângulo isósceles! ')
    else:
        print('Opção inválida! ')