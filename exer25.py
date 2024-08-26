num = int(input("Entre com um valor: "))
counter = 0
while (num != 0):
    counter += 1
    num //= 10
print("Número de digitos: ",counter)