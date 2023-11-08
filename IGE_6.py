from itertools import product
cnt = 0
for x in product('АЗПОЛЬ', repeat=6):
    q = ''.join(x)
    cnt += 1
    if q.count('Ь') <= 1 and q.count('А') == 1 and q.count('З') <=2:
        print(cnt)
        break
