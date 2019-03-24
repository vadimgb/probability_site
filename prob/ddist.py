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
