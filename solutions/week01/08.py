valor_hora = float(input("Valor por hora trabalhada: "))
horas_trab = float(input("Horas trabalhadas no mes: "))

valor_receber =  valor_hora * horas_trab

print(f"Total a receber no mês: R${valor_receber:0.02f}")

# formatação de strings - vamos ver na semana 03
# https://docs.python.org/3/library/string.html#format-specification-mini-language
