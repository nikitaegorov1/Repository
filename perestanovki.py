def permutation(str):
    if len(str)==1:
        return [str]

    all_permutations = []
    for a in str:
        for per in permutation(str.replace(a,'',1)):

            all_permutations.append((a+per)[0:4])

    return set(all_permutations)

print(permutation("1728178127"))

