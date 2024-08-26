num = int(input("Entre om um número: "))
soma = 0
while (num != 0):
    soma += num % 10
    num = num // 10
print("Soma dos digitos= ", soma)