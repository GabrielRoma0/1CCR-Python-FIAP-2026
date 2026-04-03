"""
▪ Faça um programa para a leitura de quatro notas parciais de um aluno. O programa deve calcular a
média alcançada pelo aluno e apresentar:
▪ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
▪ A mensagem "Em recuperação", se a média for entre cinco, incluindo o cinco, e sete;
▪ A mensagem "Reprovado", se a média for menor que cinco.

"""

nota1 = float(input('Digite a nota 1 : '))
nota2 = float(input('Digite a nota 2 : '))
nota3 = float(input('Digite a nota 3 : '))
nota4 = float(input('Digite a nota 4 : '))

media = (nota1+nota2+nota3+nota4)/4

if media >= 7:
    print(f'Aprovado! {media}')
elif 5 <= media < 7:
    print(f'Em recuperação! {media}')
elif 5 > media :
    print(f'Reprovado! {media}')
else:
    print(f'Opção inválida! {media}')