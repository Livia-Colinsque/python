
num = int(input("Digite um valor para num: ")) #Pedir para o usuario digitar um numero para (num)


adicao = 0 #variavel para soma


for x in range(1, num + 1):
    adicao += x  # Adiciona o valor de x à soma

# Imprime o resultado da soma
print("A soma de 1 a" ,num, "é:" ,adicao,)