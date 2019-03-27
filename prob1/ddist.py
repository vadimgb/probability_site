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
                '''dictionary - словарь, в нем 
                ключи - элементарные собыбтия, 
                значения их вероятности'''
                self.d = dictionary
        def prob(self, k):
                '''вычисляет вероятность элементарного события k'''
                if k in self.d:
                        return self.d[k]
                else:
                        return 0
        def draw(self):
                '''генерирует псевдослучайное элементарное собыите'''
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
        def conditionOnVar(self, index, val):
                res = {}
                norm = 0
                for k in self.d:
                        if k[index] == val:
                                norm += self.prob(k)
                for k in self.d:
                        if k[index] == val:
                                kn = removeElt(k, index)
                                res[kn] = self.prob(k)/norm
                return DDist(res)       
def JDist(B, AgB):
        '''B распределние сулчайной величины,
        AgB условное распределение'''
        res = {}
        for b in B.d:
                Agb = AgB(b)
                for a in Agb.d:
                        res[descartes(b, a)] = Agb.d[a] * B.d[b]
                        
        return DDist(res)

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

