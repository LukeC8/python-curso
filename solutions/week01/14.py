peso = float(input("Digite o peso do peixe: "))
excesso = peso - 50
multa = 4 * excesso

print("Excesso:", excesso)
print(f"Multa: R$ {multa:.02f}")
