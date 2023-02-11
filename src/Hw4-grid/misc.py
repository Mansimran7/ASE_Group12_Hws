import utils
from help import *
import math
import re
import sys
import copy
from copy import deepcopy
import json
from utils import *
from DATA_class import DATA

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
        print('| '*lvl + str(len(node['data'].rows)) + " ", end = '')
        if ((not node.get('left')) or (lvl==0)):
            print(node['data'].stats("mid", node['data'].cols.y, nPlaces))
        else:
            print("")
        show(node.get('left'), what, cols, nPlaces, lvl+1)
        show(node.get('right'), what, cols, nPlaces, lvl+1)

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

def transpose(t):
    u = []
    for i in range(len(t[1])):
        u.append([])
        for j in range(len(t)):
            u[i].append(t[j][i])
    return u

def last(t):
    return t[len(t)-1]

def dofile(fname):
    file = open(fname, 'r')
    temp  = re.findall(r'(?<=return )[^.]*', file.read())[0].replace('{', '[').replace('}',']').replace('=',':').replace('[\n','{\n' ).replace(' ]',' }' ).replace('\'', '"').replace('_', '"_"')
    file.close()
    f = re.sub("(\w+):", r'"\1":', temp)
    return json.loads(re.sub("(\\w+):", r'"\1":', temp))

def deepcopy(t):
    return copy.deepcopy(t)

def repRows(t, DATA, rows):
    
    rows=deepcopy(rows)
    for j,s in enumerate(rows[-1]):
        rows[0][j] = rows[0][j] + ":" + s
    
    rows.pop()
    for n,row in enumerate(rows):
        if n==0:
            row.append('thingX')
        else:
            u = t['rows'][- n]
            row.append(u[len(u) - 1])
    
    return DATA(rows)

def repCols(cols, DATA):
    cols = deepcopy(cols)
    for col in cols:
        col[len(col) - 1] = col[0] + ":" + col[len(col) - 1]
        for j in range(1, len(col)):
            col[j-1] = col[j]
        col.pop()
    
    temp = ['Num' + str(k+1) for k in range(len(cols[1])-1)]
    temp.append("thingX")
    cols.insert(0, temp)    
    return DATA(cols)

def repGrid(sFile, DATA):
    t = dofile(sFile)
    rows = repRows(t, DATA, transpose(t['cols']))
    cols = repCols(t['cols'], DATA)
    show(rows.cluster(),"mid",rows.cols.all,1)
    show(cols.cluster(),"mid",cols.cols.all,1)
    repPlace(rows)

def repPlace(data):
    n,g = 20,{}
    for i in range(1, n+1):
        g[i]={}
        for j in range(1, n+1):
            g[i][j]=' '
    
    maxy = 0
    print('')
    for r,row in enumerate(data.rows):
        c = chr(97+r).upper()
        print(c, row.cells[-1])
        x,y= row.x*n//1, row.y*n//1
        maxy = int(max(maxy,y+1))
        g[y+1][x+1] = c
    print('')
    for y in range(1,maxy+1):
        print(' '.join(g[y].values()))

