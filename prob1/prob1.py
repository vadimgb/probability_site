from random import choices
res = choices([0, 1], k = 10)
print(res)
def flips(nFlips):
        '''nFlips число бросаний монеты,
        возвращает h - частоту выпадения орла.'''
        res = choices([0, 1], k = nFlips)
        h = sum(res)/nFlips #sum(res) число выпадений орла 
        return  h
res = [flips(10) for k in range(8)]
print(res)
res = [flips(1000) for k in range(8)]
print(res)
from ddist import DDist, JDist
#H орёл, T - решка.
dm = DDist({"H":1/2, "T":1/2})
print(dm.trials(8))
PAB = DDist({("H", "H"):1/4, ("H", "T"):1/4, ("T", "H"):1/4, ("T", "T"):1/4})
PA = PAB.marginalizeOut(1)
print(PA)
def pTestGivenDis(d):
        if d == "болен":
                return DDist({"положительный":0.99, "отрицательный":0.01})
        elif d == "здоров":
                return DDist({"положительный":0.001, "отрицательный":0.999})
        else:
                raise Exception("неправильное значение для D")
print(pTestGivenDis("здоров").prob("отрицательный"))
PA = DDist({"a1":0.9, "a2":0.1})
def PBgA(a):
        if a == "a1":
                return DDist({"b1":0.7, "b2":0.3})
        else:
                return DDist({"b1":0.2, "b2":0.8})

PAB = JDist(PA, PBgA)
print(PAB)
print(PAB.conditionOnVar(1, 'b1'))
