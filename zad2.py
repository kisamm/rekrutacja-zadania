

def missingnumbers(ns, n):
    return list(set(range(n)) - set(ns))

print(missingnumbers([2, 3, 4, 7, 9], 10))


#robiłem podobne zadanie na practise python, ale bez funkcji i z różnicą, że mialem pokazać nie powtarzające się liczby

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# print(set(a) & set(b))