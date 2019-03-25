from random import random
class DDist:
        def __init__(self, dictionary):
                '''dictionary - словарь в нем 
                ключи - собыбтия, значения их вероятности'''
                self.d = dictionary
        def prob(self, k):
                '''вычисляет вероятность события k'''
                if k in self.d:
                        return self.d[k]
                else:
                        return 0
        def draw(self):
                '''генерирует псевдослучайное собыите'''
                x = random()
                help = 0
                for k in self.d:
                        help += self.d[k]
                        if help > x:
                                return k
        def trials(self, nTrials):
                '''вычисляет список из nTrials псевдослучайных событий'''
                return [self.draw() for k in range(nTrials)]
        def __repr__(self):
                return str(self.dic)
#H орел, T - решка.
dm = DDist({"H":1/2, "T":1/2})
print(dm.trials(8))
def pTestGivenDis(d):
        if d == "болен":
                return DDist({"положительный":0.99, "отрицательный":0.01})
        elif d == "здоров":
                return DDist({"положительный":0.001, "отрицательный":0.999})
        else:
                raise Exception("неправильное значение для d")
def JDist(B, AgB):
        res = {}
        for b in B.d:
                Agb = AgB(b)
                for a in Agb.d:
                        res[descartes(a, b)] = Agb.d[a] * B.d[b]
                        
        return res

def descartes(a, b):
        if type(a) == tuple and type(b) == tuple:
                return a + b
        elif type(a) == tuple:
                return a + (b,)
        elif type(b) == tuple:
                reutrn (a,) + b
        else:
                return (a, b)

PA = DDist({"a1":0.9, "a2":0.1})
def PBgA(a):
        if a == "a1":
                return DDist({"b1":0.7, "b2":0.3})
        else:
                return DDist({"b1":0.2, "b2":0.8})

PAB = JDist(PA, PBgA)
print(PAB)
