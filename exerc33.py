n = int(input("Entre com um valor: "))
print("números ímpares de 1 até {0} ".format(n))
for i in range(1, n+1):
    if (i % 2 != 0):
        print(i)
