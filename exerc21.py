num = int(input("Entrre com um número: "))
x = 0
for i in range(1, num):
    # Se a divisão do valor da variavél num for = 0  então some
    # o valor de x com o valor de I
    if (num % i == 0):
        x += i
# Se X igual a num quer dizer que é um número perfeito
if (x == num):
    print(num, "Este é um número perfeito")
else:
    print(num, "Este não é um número perfeito")