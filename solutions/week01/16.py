area = float(input("Digite a área em metros quadrados: "))
r = 1 / 3 # 0.333 litros / m2
litros_tinta = area * r
latas =  litros_tinta // 18 + (1 - ((18 - (litros_tinta % 18)) // 18)) # nota [1]
valor = 80 * latas

print(f"Precisa comprar {latas:.0f} latas")
print(f"Valor total: R$ {valor:02.02f}")

# [1] - é possivel utilizar a função math.ceil (arredondar pra cima)
