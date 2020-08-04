for n in range(100,10000):
    c=n//100
    d=n%100
    u=n%10
    if n%2==0:
        print('{} - {}'.format(n,c+d+u))
    else:
        print('{} - {}'.format(n,c*d*u))