print("x y z w")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f1 = ((x==y)and (w<=z))
                f2 = ((x<=y)<=(w==z))
                print(x,y,z,w," ",int(f1),int(f2))