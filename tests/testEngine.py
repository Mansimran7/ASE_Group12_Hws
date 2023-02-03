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

def clone_func():
    data1 = DATA(the['file'])
    data2 = data1.clone(data1.rows)
    return len(data1.rows) == len(data2.rows) and data1.cols.y[1].w == data2.cols.y[1].w and data1.cols.x[1].at == data2.cols.x[1].at and len(data1.cols.x) == len(data2.cols.x)

def around():
    data = DATA(the['file'])
    print(0,0,o(data.rows[1].cells))
    # print(0,0,data.rows[1].cells)
    for n,t in enumerate(data.around(data.rows[1])):
        if (n % 50) == 0:
            print(n, rnd(t['dist'],2) ,t['row'].cells)

def half():
    data = DATA(the['file'])
    left, right, A, B, mid, c = data.half()
    print(len(left),len(right),len(data.rows))
    print(o(A.cells),c)
    print(o(mid.cells))
    print(o(B.cells))

def cluster():
    data = DATA(the['file'])
    show(data.cluster(),"mid",data.cols.y,1)

def optimize():
    data = DATA(the['file'])
    show(data.sway(),"mid",data.cols.y,1)
