n = int(input("Entre com um valor inteiro: "))
num = n
invdertir = 0
while(n != 0):
    inverse = (invdertir * 10) + (n % 10)
    n //= 10
if(inverse == num):
    print(num, " é palíndromo.")
else:
    print(num, " Não é palíndromo.")