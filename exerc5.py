#nota
nota = int(input("Digite o valor da nota entre 0 e 20:  "))


if nota < 10:
    print("Não validada")
    
if nota >= 10 and nota <=20:
    print("Nota validada")
    
if nota >20:
    print("iNVÁLIDO")