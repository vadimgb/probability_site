from random import random
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
                return str(self.d)
        def marginalizeOut(self, i):
                '''метод DDist применятестя только
                к совместным распределениям, i индекс
                переменной которую мы хотим вынести'''
                d = {}
                for oldK in self.d:
                    k = removeElt(oldK, i)
                    incrDictEntry(d, k, self.d[oldK])
                return DDist(d)
#H орел, T - решка.
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
def JDist(B, AgB):
        '''B распределние сулчайной величины,
        AgB условное распределение'''
        res = {}
        for b in B.d:
                Agb = AgB(b)
                for a in Agb.d:
                        res[descartes(b, a)] = Agb.d[a] * B.d[b]
                        
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

PA = DDist({"a1":0.9, "a2":0.1})
def PBgA(a):
        if a == "a1":
                return DDist({"b1":0.7, "b2":0.3})
        else:
                return DDist({"b1":0.2, "b2":0.8})

PAB = JDist(PA, PBgA)
print(PAB)
