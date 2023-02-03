import utils
from help import *
import math
import re
import sys
from utils import *

# import utils

def settings(str):
    return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)",str))

def coerce(s1):
    """
        Converts value to Boolean, if value is not a boolean string it converts it to integer.
        
        Parameters
        ----------
        s : str
            value to be converted to boolean or integer
       
        Return
        ------
        int
        Bool
        """
    if s1=="true":
        return True
    elif s1=="false":
        return False
    elif s1.isnumeric():
        return int(s1)
    elif '.' in s1 and s1.replace('.','').isnumeric():
        return float(s1)
    else:
        return s1


def cli(t):
    for slot,v in t.items():
        v=str(v)
        for n,x in enumerate(sys.argv):
            if x=="-" + slot[0] or x=="--" + slot:
                if v == "false":
                    v = "true"
                elif v == "true":
                    v = "false"
                else:
                    v = sys.argv[n + 1]
        t[slot] = coerce(v)
    return t

def eg(key, str, fun):
    egs[key] = fun
    global help
    help = help + '  -g '+ key + '\t' + str + '\n'
  
def push(self,t,x):
         
        """
         Misc function to push something to the end of a list
        
        Returns
        -------
        pushed element
        """
        t.append(x) # if t is list
        return x

def sort(self,t,x):
         
        """
         Misc function to sort something to the end of a list
        
        Returns
        -------
        pushed element
        """
        t.sort() # if t is list
        return t

def kap(t, fun):
    x = {}
    for i in t:
        k = t.index(i)
        i, k =fun(k,i)
        x[k or len(x)] = i
    return x

def show(node, what, cols, nPlaces, lvl = 0):
    if node:
        lvl = lvl or 0
        # iowrite command
        print((not node.left) or (lvl==0)) and o(node.data.stats("mid", node.data.cols.y, nPlaces) or "")
        show(node.left, what, cols, nPlaces, lvl+1)
        show(node.right, what, cols, nPlaces, lvl+1)

def cosine(a, b, c):
    temp = 1 if c == 0 else 2*c
    x1 = (a**2 + c**2 - b**2) // temp
    x2 = max(0, min(1, x1))
    y = abs((a**2 - x2**2))**0.5
    return x2, y

def any(t):
    return t[rint(0, len(t) - 1)]

def many(t, n):
    u = []
    for i in range(1, n+1):
        u.append(any(t))
    return u