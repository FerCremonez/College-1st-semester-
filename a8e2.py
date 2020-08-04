num=int(input('Insira o número: '))
if num < 0:
    print('Não existe fatorial de números negativos.')
else:
    fat=1
    for i in range(num,1,-1):
        fat*=i
print('Fatorial=',fat)
