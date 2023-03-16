# importing all the required libraries
import math
from help import *
import misc
from misc import *
import io
import os
import sys

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
    temp_dict = t.__dict__
    temp_dict['a'] = t.__class__.__name__
    temp_dict['id'] = id(t)
    print(dict(sorted(temp_dict.items())))
    return t

def rint(low, high, Seed = None):

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
    return math.floor(0.5 + rand(low,high, Seed))

def rand(low, high, mSeed = None):
    
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
    global Seed
    Seed = 1 if mSeed else (16807 * Seed) % 2147483647
    result = low + (high-low) * Seed / 2147483647
    return result

def rnd(x, places = 3):
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
    mult = pow(10, places or 3)
    return math.floor(x * mult + 0.5) / mult

def csv(sFilename, fun):
    if sFilename:
        src = io.open(sFilename)
        t = []
        for _,l in enumerate(src):
            s = l.strip().split(',')
            r = list(map(misc.coerce, s))
            t.append(r)
            fun(r)
    else:
        print("File not opening")
        
        
