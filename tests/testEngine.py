import random
import csv
import sys
sys.path.append(sys.path[0]+'\\..\\src\\')
from num_class import Num
from sym_class import Sym
from misc import *
from utils import *

eg={}

def sym():
    """
    Test for symbols
    
    Returns
    -------
    Bool
    """
    sym = Sym()
    symbols = ["a","a","a","a","b","b","c"]
    for x in symbols:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    entropy = 1000*entropy//1/1000
    oo({"mid":mode,"div":entropy})
    return (mode =="a" and 1.37 <= entropy and entropy <= 1.38) 

def num():
    """
    Test for numbers
    
    Returns
    -------
    Bool
    """
    num = Num()
    for i in range(1,101):
        num.add(i)
    mid = num.mid()
    div = num.div()
    print(mid,div)
    return (50<=mid and mid<=52 and 30.5<div and div<32)

    
def ALL():
    """
    Runs all the tests
        
    Returns
    -------
    Bool
    """
    fails=0
    l = LIST()
    for task in l:
        if task != "ALL":
            if not runs(task):
                fails = fails + 1
    return True

eg["ALL"]= ALL,
eg["sym"]= sym,
eg["num"]= num