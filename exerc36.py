n=int(input("digite um valor inteiro: "))
r=0
while(n>0):
    r = r * 10  
    r = r+ n%10
    n = int( n/10)
print(r)