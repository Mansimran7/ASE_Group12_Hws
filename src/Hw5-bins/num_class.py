import math
import random
from utils import rnd
from help import the

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
        Calculates the mean for Nums.
    """

    def __init__(self, at=None, txt=None):
        self.at = at if at else 0
        self.txt = txt if txt else ""
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = math.inf
        self.hi = -math.inf
        self.w = -1 if "-" in self.txt else 1
        self.has = {}


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
            if self.n <= the['Max']:
                self.has[v]= v
            d = v - self.mu
            self.mu = self.mu + d/self.n
            self.m2 = self.m2 + d*(v - self.mu)
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
        return self

    def div(self):
        """
        Calculates the standard deviation of Nums.

        Parameters
        ----------
        Returns
        -------
        int
        """
        return 0 if (self.m2 <0 or self.n < 2) else (self.m2/(self.n-1))**0.5

    def mid(self):
        """
        Calculates the mean for Nums.

        Parameters
        ----------
        Returns
        -------
        int
        """
        return self.mu
    
    def rnd(self,a,n):
        """
        returns rounded number
        """
        return a if a == "?" else rnd(a,n)
    
    def norm(self, n):
        
        if n=="?":
            return n
        else:
            return (n - self.lo)/(self.hi - self.lo + math.pow(10, -32))
    
    def dist(self, n1, n2):

        if n1=="?" and n2=="?":
            return 1
        
        n1, n2 = self.norm(n1), self.norm(n2)

        if n1=="?":
            if n2 < 0.5:
                n1 = 1
            else:
                n1 = 0
        
        if n2=="?":
            if n1<0.5:
                n2 = 1
            else:
                n2 = 0

        return abs(n1-n2)
    
