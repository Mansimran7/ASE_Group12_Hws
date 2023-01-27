import random
import sys
sys.path.append(sys.path[0]+'\\..\\src\\')
from num_class import Num
from sym_class import Sym
from DATA_class import DATA
from utils import *
from misc import *
import math


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
    return (mode =="a" and 1.379 == rnd(entropy,3))

def num():
    """
    Test for numbers
    
    Returns
    -------
    Bool
    """
    num = Num()
    numbers=[1,1,1,1,2,2,3]
    for i in numbers:
        num.add(i)
    mid = num.mid()
    div = num.div()
    return (11/7 == mid and 0.787 == rnd(div,3))

def the_func():
    """
    Test for the
    
    Returns
    -------
    Bool
    """
    oo(the)
    return True

def the_rand():

    """
    Runs all rand function
        
    Returns
    -------
    Bool
    """

    num1 = Num()
    num2 = Num()
    global Seed
    Seed=the['seed']
    for i in range(1, 1001):    
        num1.add(rand(0,1))
    Seed=the['seed']
    for i in range(1, 1001):
        num2.add(rand(0,1))
    m1 = rnd(num1.mid(), 1)
    m2 = rnd(num2.mid(), 1)
    return m1==m2 and 0.5==rnd(m1, 1)

def num_chars(t):
    global n
    n = n + len(t)

def csv_test():
    csv(the['file'],num_chars)
    return n == 8*399

def data():
    data = DATA(the['file'])
    len_of_rows = len(data.rows)
    return len_of_rows == 398 and data.cols.y[0].w == -1 and data.cols.x[1].at == 1 and len(data.cols.x) == 4

def stats():
    data = DATA(the['file'])
    for k, cols in {'y': data.cols.y, 'x':data.cols.x}.items():
        print(k, 'mid',data.stats('mid',cols,2))
        print(' ','div', data.stats('div',cols,2))
    return True

