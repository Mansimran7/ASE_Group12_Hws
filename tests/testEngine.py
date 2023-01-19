import random
import sys
sys.path.append(sys.path[0]+'\\..\\src\\')
from num_class import Num
from sym_class import Sym
from utils import *
from misc import *

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
    #oo({"mid":mode,"div":entropy})
    return (mode =="a" and 1.379 == entropy and rnd(entropy,3))

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
    #print(mid,div)
    return (50<=mid and mid<=52 and 30.5<div and div<32)

def the_func():
    """
    Test for the
    
    Returns
    -------
    Bool
    """
    oo(the)
    return True

def runs(k):
    """
    Resets random number seed before running something ,Cache the detaults settings and restore them after the test
    Print error messages or stack dumps as required or Return true if this all went well. 

    Parameters
    ----------
    k : dict
        the['eg']
    p   : int
        position from which to get the number in the list    
    
    Returns
    -------
    Bool
    """
    if k not in eg:
        return
    old = {}
    for t in the:
        old[t]=the[t]
    try:
        status = eg[k]()
        if status == True:
            message = "PASS"
        elif status == None:
            message = "CRASH"
        else:
            status = True
            message = "FAIL"
    except:

        status = False
        message = "CRASH"
    for t in old:
        the[t]=old[t]
    if status==True:
        print("✅ pass:",k)
    else:
        print("❌ fail:",k)
    #print("\n!!!!!", message, k, status)
    #print(("-"*50)+"\n")
    return status

def LIST():
    """
    Sort all test names
        
    Returns
    -------
    list
    """
    t=[] 
    for k in eg:
        t.append(k)
    t.sort() 
    return t

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

eg["ALL"]= ALL
eg["sym"]= sym
eg["num"]= num
eg["the"]= the_func
