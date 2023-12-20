def f(i):
    x=bin(i)
    x1=x[2:]
    y=bin(i%3)
    y1=y[2:]
    z=x1+y1
    v=bin(int(z)%5)
    v1=v[2:]
    t=z+v1
    t1=int(t,2)
    return t1
k=0
for i in range(1111111110//32,1444444416//32):
    p=f(i)
    if p >= 1111111110 and p <= 1444444416:
        k += 1
print(k)
