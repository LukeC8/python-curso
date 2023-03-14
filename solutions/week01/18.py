tamanho_MB = float(input("Digite o tamanho do arquivo em MB: "))
link_mbps = float(input("Digite a velocidade do link (Mbps): "))

tamanho_Megabit = 8 * tamanho_MB # 1 Byte tem 8 bits

tempo_min = tamanho_Megabit / link_mbps / 60

print(f"Tempo aproximado em minutos: {tempo_min}")

# Nota
# MB é a sigla para Mega (10^6) Byte
# Mbps é a sigla para Mega (10^6) bits por segundo
