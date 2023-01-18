import math
import random
from maths import per
from misc import the

class Num:
    """
    A class to represent a Number to summarize a stream of symbols.

    ...

    Attributes
    ----------
    n : int
        the number of items seen so far
    at : int
        the column position
    name : str
        the name of the column
    has : dict
        list of all the data sored in a column
    lo : int
        the lowest  number seen so far
    hi : int
        the highest number seen so far
    isSorted: Bool
        stores whether the data is in sorted order or not

    Methods
    -------
    nums():
        identifies if numbers are sorted or not and if not sorts them in ascending order.
    add(v):
        Increments the total no. of numbers seen so far and total no. of a particular number seen so far by
        maintaining a Reservoir sampler.
    div():
        Calculates the standard deviation of Nums.
    mid():
        Calculates the median for Nums.
    """

    def __init__(self, c = 0 , s = ""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = []
        self.lo = math.inf
        self.hi = -math.inf
        self.isSorted = True
    
    def nums(self):
        """
        identifies if numbers are sorted or not and if not sorts them in ascending order and returns the sorted Numbers.

        Parameters
        ----------
        
        Returns
        -------
        dict
        """
        if not self.isSorted:
            self._has.sort()
            self.isSorted=True
        return self._has

    def add(self, v):
        """
        Increments the total no. of numbers seen so far and total no. of a particular number seen so far by
        maintaining a Reservoir sampler that keeps at most the.nums numbers which are uniformally spaced. 
        And if we run out of room, delete something old, at random.

        Parameters
        ----------
        v : str
            does nothing for v = '?'

        Returns
        -------
        None
        """
        if v!="?":
            self.n = self.n+1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < the["nums"]:
                self._has.append(v)
            else:
                pos = random.randint(0,len(self._has)-1)
                self.isSorted = False
                self._has[pos] = v

    def div(self):
        """
        Calculates the standard deviation of Nums.

        Parameters
        ----------
        Returns
        -------
        int
        """
        return (per (self.nums(),0.9)-per(self.nums(),0.1))/2.58

    def mid(self):
        """
        Calculates the median for Nums.

        Parameters
        ----------
        Returns
        -------
        int
        """
        return per(self.nums(), 0.5)