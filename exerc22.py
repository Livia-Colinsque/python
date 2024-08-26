num = int(input("Entre com um valor : "))
primeiro = True
'''
// - Este operador retorna apenas a parte inteira da divisão entre os operandos,
arredondando para baixo para o inteiro mais próximo
'''

for i in range(2, num // 2 + 1):
    if (num % i == 0):
        primeiro = False
        break
if (primeiro == 1):
    print(num, " é o primeiro")
else:
    print(num, " Este não é o primeiro")