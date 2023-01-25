import math

class Sym:
    """
    A class to represent a Symbol to summarize a stream of symbols.

    ...

    Attributes
    ----------
    n : int
        the number of items seen
    at : int
        the column position
    name : str
        the name of the column
    has : dict
        stores the no. of occurances of a particular symbol

    Methods
    -------
    add(v):
        Increments the total no. of symbols seen so far and total no. of a particular symbol seen so far.
    mid():
        Calculates the mode in the has dictionary.
    div():
        Calculates the diversity of a symbol.
    """

    def __init__(self):
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self, v):
        """
        Increments the total no. of symbols seen so far and total no. of a particular symbol seen so far.

        Parameters
        ----------
        v : str
            does nothing for v = '?'

        Returns
        -------
        None
        """
        if v!="?":
            self.n=self.n+1
            self.has[v] = 1 + (self.has[v] if v in self.has.keys() else 0)
            if self.has[v] > self.most:
                self.most = self.has[v]
                self.mode = v

    def mid(self):
        """
        Calculates the mode(most commonly seen symbol) in the has dictionary.

        Parameters
        ----------
        Returns
        -------
        int
        """
        return self.mode

    def div(self):
        """
        Calculates the diversity of symbol by calculating its entropy.

        Parameters
        ----------
        Returns
        -------
        int
        """
        def fun(p):
            return p*(math.log(p,2))
        e=0
        for k in self.has:
            n=self.has[k]
            e=e+fun(n/self.n)
        return -e
    
    def rnd(self, v, n):
        return self.v
