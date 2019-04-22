def removeElt(k, i):
        '''Удаляет из k  события i элемент'''
        result = k[:i] + k[i+1:] 
        if len(result) == 1: 
                return result[0] 
        else: 
                return result

def incrDictEntry(d, k, v):
        '''В словарь d значение для
        ключа k увеличивает на v''' 
        if k in d: 
                d[k] += v 
        else: 
                d[k] = v

class DDist(dict):
        def marginalizeOut(self, i):
                '''метод  применяется только
                к совместным распределениям, i индекс
                переменной которую мы хотим вынести'''
                d = DDist() 
                for oldK in self:
                    k = removeElt(oldK, i)
                    incrDictEntry(d, k, self[oldK])
                return d 

p1=DDist(H=0.5, T=0.5)
print(p1)
def JDist(B, AgB):
        '''B распределение случайной величины,
        AgB условное распределение'''
        res = DDist() 
        for b in B:
                Agb = AgB(b)
                for a in Agb:
                        res[descartes(b, a)] = Agb[a] * B[b]
                        
        return res

def descartes(a, b):
        '''Вспомогательная функция
        объединяет значения величин в tuple'''
        if type(a) == tuple and type(b) == tuple:
                return a + b
        elif type(a) == tuple:
                return a + (b,)
        elif type(b) == tuple:
                reutrn (a,) + b
        else:
                return (a, b)

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
def makeProbField(name, omega):
        '''omega объект класса DDist, 
         функция возвращает класс событие
        с именем name'''
        def __init__(self, pred):
                '''pred предикат выбирающий элементарные
                события удовлетворяющие условию,
                задаёт событие'''
                self.samples = {k for k in self.omega if pred(k)}

        @property
        def prob(self):
                '''свойство - вероятность собыитя'''
                return sum([self.omega[k] for k in self.samples])

        def __add__(self, over):
                '''задаёт сумму событий'''
                f = lambda x: (x in self.samples or x in over.samples)
                return makeProbField(name, omega)(f)

        def __mul__(self, over):
                f = lambda x: (x in self.samples and x in over.samples)
                return makeProbField(name, omega)(f)

        def __sub__(self, over):
                f = lambda x: x in self.samples and not x in over.samples
                return makeProbField(name, omega)(f)
        def __str__(self):
                return str(self.__class__.__name__) + str(self.samples)

        return type(name, (object,), dict(omega=omega,
         __init__ = __init__, prob=prob, __add__=__add__, __mul__=__mul__, 
        __sub__=__sub__, __str__=__str__))
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
