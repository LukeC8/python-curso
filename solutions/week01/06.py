raio = int(input("Digite o raio do círculo: "))

pi = 3.14159
area_circulo = pi * (raio * raio)

print("A área do círculo de raio", raio, "é", area_circulo)

# usando format string - Qual a diferença?
print(f"A área do círculo de raio {raio} é {area_circulo}")
