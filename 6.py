for a in range(1, 500):
    f = True
    for x in range(1, 500):
        for y in range(1, 500):
            if ((x+2*y)>48 or (y>x) or (x+3*y<a))==0:
                f = False
    if not f:
        print(a)