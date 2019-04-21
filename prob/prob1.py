def makeProbField(name, omega):
        '''omega словарь элементарных событий и
        их вероятностей, возвращает класс событие
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
p = Fraction('1/6')
Cube = makeProbField("Cube", {1:p, 2:p, 3:p, 4:p, 5:p, 6:p})
a = Cube(lambda x: x % 2 == 0)
b = Cube(lambda x: x > 3)
d = a + b
print(f"{a} prob={a.prob}")
print(f"{b} prob= {b.prob}")
print(f"{d} prob = {d.prob}")