ft = int(input("Digite a quantidade de fotocópias: "))

if ft <= 10:
    print ("Total a pagar: " , ft * 0.25)

if ft >10 and ft <=20:
    print ("O total a pagar é: ", ft * 0.20)
    
if ft >20:
    print ("O total a pagar é: ",  ft * 0.10)
    
