# VOTO OPCIONAL OU NAO
# 0 a > 16 anos não vota e < 70 anos)
# <= 16 e <18 = opcional e > 70 anos)
# Resto = obrigatório

idade = int(input('Digite sua idade :'))

#NÃO PODEM VOTAR
if idade < 16:
    print('Não é possível votar! ')

#VOTO OPCIONAL
elif 17 >= idade >= 16:
    print('Voto opcional')
elif idade > 70:
    print('Voto opcional')

#VOTO OBRIGATÓRIO
else:
    print('Voto obrigatório!')


