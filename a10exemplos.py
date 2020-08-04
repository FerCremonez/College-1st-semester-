'''notas=[7.5,4.5,8,3,9.5]
soma=0
for i in range(5):
    soma+=notas[i]
med=soma/5
print(med)

a=[0]*10'''


'''A=[0]*10
print('Digite os elementos:')
for i in range(10):
    A[i]=(int(input()))'''

#exemplo leitura de 50 notas
notas=[]  #lista com valores zerados
s=0       #variavel de soma

print('Digite as notas')

for i in range(5):
    notas.insert(i,float(input()))

for i in range(5):
    s += notas[i]

med=s/5
print('A média das notas é:',med)