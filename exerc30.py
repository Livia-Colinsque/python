num1 = int(input("Entre com o valor 1 : "))
num2 = int(input("entre com o valor 2 : "))
min = num1 if (num1 < num2) else num2

for i in range(1, min+1) :
    if (num1 % i == 0 and num2 % i == 0):
        gcd = i
# GCD - Greatest Common Factor "Maior Fator comun"
print("GCD of {0} e {1} = {2}".format(num1, num2, gcd))