class DDist:
        def __init__(self, dictionary):
                self.d = dictionary
        def draw(self):
                x = random()
                help = 0
                for k in self.d:
                        help += self.d[k]
                        if help > x:
                                return k
</pre>

<img src = "fig.png">

