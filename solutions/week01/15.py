valor_hora = float(input("Digite o valor da hora de trabalho: "))
horas_trab = float(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = horas_trab * valor_hora
ir = salario_bruto * .11
inss = salario_bruto * .08
sindicato = salario_bruto * .05
liquido = salario_bruto - ir - inss - sindicato

print(f"Salário Bruto: R$ {salario_bruto:02.02f}")
print(f"IR (11%): R$ {ir:02.02f}")
print(f"INSS (8%): R$ {inss:02.02f}")
print(f"Sindicato (5%): R$ {sindicato:02.02f}")
print(f"Salário Líquido: R$ {liquido:02.02f}")
