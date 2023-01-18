import math
from misc import the,coerce

def o(t):
    """
       o is a telescope that generates a string from a nested table.

       Parameters
       ----------
        t : dict
            the nested dictionary to be converted to a string form
       
       Returns
       -------
       str
    """
    if type(t)!=dict:
        return str(t)
    def show(k,v):
        if "^_" not in str(k):
            v=o(v)
            return str(k)+" : "+str(v)
    u=[]
    for k in t:
        u.append(show(k,t[k]))
    if len(t)==0:
        u.sort()
    return " ".join(u)

def oo(t):
    """
        oo are some binoculars we use to exam stucts. It prints the string from 'o'
        
        Returns
        -------
        str
        """
    print(o(t))
    return t

seed=937162211
def rint(low, high):

    """
    Returns a integer value closest to specified value
        
    Parameters
    ----------
    low : int
        lower bound
    places  : int
        upper bound 

    Returns
    -------
    int
    """
    
    return math.floor(0.5 + rand(low, high))

def rand(low, high):
    
    """
    Returns a random number between 0 and 1
        
    Parameters
    ----------
    low : int
        lower bound
    places  : int
        upper bound 

    Returns
    -------
    int
    """
    
    low = low or 0
    high = high or 1
    seed = (16807 * seed) % 2147483647
    result = low + (high-low) * seed / 2147483647
    return result

def rnd(x, places):
    """
        Rounds of to nearest integer upto specified places.
        
        Parameters
        ----------
        x : int
            number to be rounded
        places  : int
                  upto number of places to be rounded 

        Returns
        -------
        int
        """
    mult = pow(10, places or 2)
    return math.floor(x * mult + 0.5) / mult

def csv(fname, sep=None, src=None, s=None, t=None):
    """
        Reads the csv file and  Call fun() on each row to add the rows in the data object.
        Row cells are divided in the.seperator.

        Parameters
        ----------

        fname : str
                location of the csv file to be read
        
        Returns
        -------
        None
        """
    sep = the["sep"]
    with open(fname) as src:
        while s := src.readline().rstrip():
            t = {}
            for y in s.split(sep):
                print(y)
                try:
                    t[1 + len(t)] = coerce(y)
                except:
                    pass