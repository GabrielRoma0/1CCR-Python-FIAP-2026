lista_frutas = ['Banana', 'Morango', 'Manga']

#lista_frutas[0] = 'Banana'
#lista_frutas[1] = 'Morango'
#lista_frutas[2] = 'Manga'

print(lista_frutas[1])

# Manipulando arrays
# append(nova fruta)

lista_frutas.append('Goiaba')
print(lista_frutas[-1]) # Seleciona o último elemento da lista
print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

# Fruta foi decidido baseado na lista
for fruta in lista_frutas:
    print(fruta)


