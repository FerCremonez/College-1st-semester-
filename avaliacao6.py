num=int(input('Insira o número:'))  #entrada
soma=0  #contador
if num==1:
    print('É quadrado perfeito')
else:
    for i in range(1,num,2):
        soma+=i
        if soma==num:
            print('É quadrado perfeito')
            break
    else:
         print('NÃO É quadrado perfeito')
