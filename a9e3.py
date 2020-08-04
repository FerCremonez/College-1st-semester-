for num in range (1000,10000):
    a=num//100
    b=num%100
    c=a+b
    if pow(c,2)==num:   
        print(num)