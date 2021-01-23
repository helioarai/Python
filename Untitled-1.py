'''eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print (eng2sp)
print(eng2sp['one'])
vals = eng2sp.values()
print( 'uno' in vals)
print(vals)
chaves=eng2sp.keys()
print(chaves)'''

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

j=histogram('brontossauro e gigante e muito feio de ser visto dentro do espectro do microscópio')
for c in sorted(j):
    print(c, j[c])
print (j)