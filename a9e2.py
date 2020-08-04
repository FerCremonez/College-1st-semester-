n=int(input("Digite a quantidade dee elementos da série:"))
a=0
b=1
for cont in range(1,n+1):
    c=a+b
    print(c)
    b=a
    a=c