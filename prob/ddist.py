from random import choices
res = choices([0, 1], k = 10)
print(res)
def flips(nFlips):
        '''nFlips число бросаний монеты,
        возвращает h - частоту выпадения орла.'''
        res = choices([0, 1], k = nFlips)
        h = sum(res)/nFlips 
        return  h
res = [flips(10) for k in range(8)]
print(res)
res = [flips(1000) for k in range(8)]
print(res)
