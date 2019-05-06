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
        def conditionOnVar(self, index, val):
                res = DDist() 
                norm = 0
                for k in self:
                        if k[index] == val:
                                norm += self[k]
                for k in self:
                        if k[index] == val:
                                kn = removeElt(k, index)
                                res[kn] = self[k]/norm
                return res      
        def condDist(self, index):
                '''Только для совместного распределена,
                находит условное распределение'''
                return lambda x: self.conditionOnVar(index, x)

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
        if isinstance(a, tuple) and isinstance(b, tuple):
                return a + b
        elif isinstance(a, tuple):
                return a + (b,)
        elif isinstance(b, tuple):
                reutrn (a,) + b
        else:
                return (a, b)

def bayes(pA, PBgA, b):
        return JDist(pA, PBgA).conditionOnVar(1, b)
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
