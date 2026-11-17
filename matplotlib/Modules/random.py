class Random:
    def __init__(self, seed):
        self.__seed = seed

    def generate(self, a: int = None, b: int = None, c: int = None):
        if a and b and c:
            self.__seed = (a * self.__seed + b) % c
            return self.__seed
        elif a == b == c and a is None:
            s = str(self.__seed**2)
            while len(s) != 12:
                s = "0" + s
            self.__seed = int(s[3:9])
            return self.__seed
        else:
            raise Exception('There are no method with these parameters.')

    def __str__(self):
        return f'{self.generate()}'
