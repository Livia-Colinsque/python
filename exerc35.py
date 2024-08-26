n = int(input("Entre com um valor inteiro: "))
ultimo = n % 10
primeiro = n
while(primeiro >= 10):
    primeiro = primeiro //10
print("Primeiro digito = ", primeiro)
print("último digito = ", ultimo)