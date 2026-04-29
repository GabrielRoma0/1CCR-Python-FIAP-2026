def verificar_nota(nota):  # Função para poupar linhas para verificar nota
    while 10 < nota or nota < 0:
        print('A nota deve estar entre 0 e 10')
        nota = float(input('Digite a nota novamente: '))
    return nota #garantir que o while rode

notaA = float(input('Digite a 1 nota: '))
notaA = verificar_nota(notaA)

notaB = float(input('Digite a 2 nota: '))
notaB = verificar_nota(notaB)

media = (notaA + notaB) / 2
print(media)
