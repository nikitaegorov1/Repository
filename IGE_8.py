x = 1331**650-55*121**610+77*11**510-3*11**100-221
def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result
z =convert_to(x,11)
print(z.count('a'))