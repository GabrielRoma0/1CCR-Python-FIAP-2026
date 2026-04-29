cp = 0
while cp < 10:
    cp += 1

    if cp == 3 and cp == 5 :    # Para não exibir o 3 e o 5
        continue                # E continuar após ele

    if cp == 7:    # Não exibe o 7
        break      # Para aqui

    print(f'Produto {cp}')


# while decrescente de 4 até 1
i = 4
while i >= 1:
    print(i)
    i -= 1



