"""
▪ Faça um programa que recebe:
▪ o código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5
▪ o peso da carga do caminhão em toneladas
▪ o código da carga, supondo que é um número inteiro de 10 e 40
▪ Seu programa deve calcular:
▪ o peso da carga do caminhão convertido em quilos
▪ o preço da carga do caminhão
▪ valor do imposto que e cobrado com base no preço da carga e do estado de origem
▪ o valor total transportado pelo caminhão (carga + impostos)

TABELA ESTÁ NO SLIDE

"""

cod_est = int(input('Digite o código de origem da carga (1 a 5): '))
pes_ton = float(input('Digite o peso da carga em toneladas: '))
cod_car = int(input('Digite o código da carga (10 a 40): '))

# Convertendo toneladas para quilos (se o enunciado pedir kg)
pes_kg = pes_ton * 1000

# 1. Definir o preço por quilo baseado no código da carga
if 10 <= cod_car <= 20:
    preco_quilo = 100
elif 21 <= cod_car <= 30:
    preco_quilo = 250
elif 31 <= cod_car <= 40:
    preco_quilo = 340
else:
    preco_quilo = 0
    print("Código de carga inválido!")

# 2. Calcular preço total da carga
preco_carga = pes_kg * preco_quilo

# 3. Definir a porcentagem do imposto
if cod_est == 1:
    imposto_percentual = 0.35
elif cod_est == 2:
    imposto_percentual = 0.25
elif cod_est == 3:
    imposto_percentual = 0.15
elif cod_est == 4:
    imposto_percentual = 0.05
elif cod_est == 5:
    imposto_percentual = 0.0  # Isento
else:
    imposto_percentual = 0.0
    print("Código de estado inválido!")

# 4. Cálculos finais
valor_imposto = preco_carga * imposto_percentual
valor_total = preco_carga + valor_imposto

# Exibição dos resultados
print(f'\nPreço da carga: R$ {preco_carga:.2f}')
print(f'Valor do imposto: R$ {valor_imposto:.2f}')
print(f'Valor total: R$ {valor_total:.2f}')