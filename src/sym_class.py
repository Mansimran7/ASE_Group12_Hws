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

    def __init__(self, c = 0, s = ""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = dict()

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
            if v in self._has:
                self._has[v] += 1
            else:
                self._has[v] = 1

    def mid(self):
        """
        Calculates the mode(most commonly seen symbol) in the has dictionary.

        Parameters
        ----------
        Returns
        -------
        int
        """
        most=-1
        for k in self._has:
            v=self._has[k]
            if v>most:
                mode, most=k,v
        return mode

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
        for k in self._has:
            n=self._has[k]
            if n>0:
                e=e-fun(n/self.n)
        return e