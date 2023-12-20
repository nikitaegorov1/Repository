def Div(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return n > 1
def fn(u):
    A = '0' + u
    while '01' in A or '02' in A:
        A = A.replace('02','1110',1).replace('01','220',1)
    return 1 if Div(sum(map(int, list(A)))) else 0
s=[]
for x in range(1,100):
    for y in range(1,100):
        if (x+y)>=39 and fn("1"*x + "2"*y):
            s.append(1*x + 2*y)
print(min(s))
