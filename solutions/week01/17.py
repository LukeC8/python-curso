import math

area = float(input("Digite a area em metros quadrados: "))
r = 1 / 6
preco_lata = 80
quantidade_lata = 18
preco_galao =  25
quantidade_galao = 3.6

litros_tinta = area * r  # sem 10% de folga
# litros_tinta = area * r * 1.1

total_latas = math.ceil(litros_tinta / quantidade_lata)
total_galao = math.ceil(litros_tinta / quantidade_galao)

print(f"Quantidade de tinta necessária: {litros_tinta:.03f} litros")
print(f"Preço comprando apenas latas: {total_latas * preco_lata:.03f}")
print(f"Preço comprando apenas galões: {total_galao * preco_galao:.03f}")

litros_tinta *= 1.1
total_latas = litros_tinta // quantidade_lata
total_galao =  math.ceil((litros_tinta % quantidade_lata) / quantidade_galao)

print("\n\nMisturando galoes e latas:")
print(f"Total de litros (com 10% de folga): {litros_tinta:.03f} litros")
print(f"Quantidade de latas: {total_latas:.03f}")
print(f"Quantidade de galões: {total_galao:.03f}")
print(f"Preço: {total_latas * preco_lata + total_galao * preco_galao:.03f}")
