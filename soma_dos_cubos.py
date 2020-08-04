for i in range (100,999):
    c=i//100
    d=i%100//10
    u=i%10
    a=pow(c,3)
    b=pow(d,3)
    c=pow(u,3)
    if a+b+c==i:
        print(i)
