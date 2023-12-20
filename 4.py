k=0
for i in range(2024,10**10,2024):
    s=str(i)
    if s[0]=="3" and s[2:6]=="6906" and s[-1] == "4":
        print(i,i//273)
        k+=1
print(k)
