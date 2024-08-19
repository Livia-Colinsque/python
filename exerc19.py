num = int(input("Digite o numero que voce quer saber a tabuada: "))

for x in range(1, 11):
    resultado = num * x  # Calcula a tabuada
    print(f"{num} x {x} = {resultado}")  # Exibe o resultado