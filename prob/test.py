from ddist import *
PA = DDist({'a1':0.9, 'a2':0.1})
def PBgA(a):
        if a == 'a1':
                return DDist({'b1':0.7, 'b2':0.3})
        else:
                return DDist({'b1':0.2, 'b2':0.8})

PAB = JDist(PA, PBgA)
print(PAB)
PAB = DDist({('H', 'H'):1/4, ('H', 'T'):1/4, ('T', 'H'):1/4, ('T', 'T'):1/4})
PA = PAB.marginalizeOut(1)
print(PA)
print(PAB.conditionOnVar(1,"H"))
pDis=DDist({True: 0.001, False: 0.999})
def pTestGivenDis(disease):
        if disease:
                return DDist({True: 0.99, False: 0.01})
        else:
                return DDist({True: 0.001, False: 0.999})

print(bayes(pDis, pTestGivenDis, True))
from fractions import Fraction
p = Fraction(1, 6)
pCube = DDist({1:p, 2:p, 3:p, 4:p, 5:p, 6:p})
Cube = makeProbField('Cube', pCube)
a = Cube(lambda x: x % 2 == 0)
b = Cube(lambda x: x > 3)
d = a + b
print(f'{a} prob={a.prob}')
print(f'{b} prob= {b.prob}')
print(f'{d} prob = {d.prob}')
