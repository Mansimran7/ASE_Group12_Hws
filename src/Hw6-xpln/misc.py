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
from sym_class import Sym

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

def dkap(t, fun):
    u = {}
    if t == -1:
        t = (-1, -1)
    for k,v in t.items():
        v, k = fun(k,v) 
        u[k or len(u)] = v
    return u

def showTree(node, what, cols, nPlaces, lvl = 0):
  if node:
    print('|.. ' * lvl + '[' + str(len(node['data'].rows)) + ']' + '  ', end = '')
    if not node.get('left') or lvl == 0:
        print(node['data'].stats("mid",node['data'].cols.y,nPlaces))
    else:
        print('')
    showTree(node.get('left'), what,cols, nPlaces, lvl+1)
    showTree(node.get('right'), what,cols,nPlaces, lvl+1)

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

def cliffsDelta(ns1, ns2):
    if(len(ns1)>256):
        ns1 = many(ns1, 256)
    if(len(ns2)>256):
        ns2 = many(ns2, 256)
    if(len(ns1)>10*len(ns2)):
        ns1 = many(ns1, 10*len(ns2))
    if(len(ns2)>10*len(ns1)):
        ns2= many(ns2, 10*len(ns1))
    
    n, gt, lt = 0, 0, 0
    for _,x in enumerate(ns1):
        for _,y in enumerate(ns2):
            n+=1
            if x > y:
                gt = gt + 1
            if x < y: 
                lt = lt + 1
    
    return abs(lt-gt)/n > the['cliffs']

def diffs(nums1, nums2):
    return kap(nums1, cliffsDelta(nums['has'], nums2[k]['has'], nums.txt))

def bins(cols, rowss):
    out =[]
    for col in cols:
        ranges = {}
        for y, rows in rowss.items():
            for row in rows:
                x = row.cells[col.at]
                if x!= '?':
                    k = int(bin(col,x))
                    if not k in ranges:
                        ranges[k] = RANGE(col.at, col.txt, x)
                    extend(ranges[k], x, y)
        ranges = list(dict(sorted(ranges.items())).values())
        if(isinstance(col, Sym)):
            r = ranges
        else:
            r = mergeAny(ranges)
        out.append(r)
    return out

def bin(col,x):
    if x=="?" or isinstance(col, Sym):
        return x
    tmp = (col.hi - col.lo)/(the['bins'] - 1)
    return  1 if col.hi == col.lo else math.floor(x/tmp + 0.5)*tmp

def merge(col1,col2):
  new = deepcopy(col1)
  if isinstance(col1, Sym):
      for n in col2.has:
        new.add(n)
  else:
    for n in col2.has:
        new.add(new,n)
    new.lo = min(col1.lo, col2.lo)
    new.hi = max(col1.hi, col2.hi) 
  return new

def RANGE(at,txt,lo,hi=None):
    return {'at':at,'txt':txt,'lo':lo,'hi':lo or hi or lo,'y':Sym()}

def extend(range,n,s):
    range['lo'] = min(n, range['lo'])
    range['hi'] = max(n, range['hi'])
    range['y'].add(s)

def itself(x):
    return x

def value(has,nB = None, nR = None, sGoal = None):
    sGoal,nB,nR = sGoal or True, nB or 1, nR or 1
    b,r = 0,0
    for x,n in has.items():
        if x==sGoal:
            b = b + n
        else:
            r = r + n
    b,r = b/(nB+1/float("inf")), r/(nR+1/float("inf"))
    return b**2/(b+r)


def merge2(col1,col2):
  new = merge(col1,col2)
  if new.div() <= (col1.div()*col1.n + col2.div()*col2.n)/new.n:
    return new

def mergeAny(ranges0):
    def noGaps(t):
        for j in range(1,len(t)):
            t[j]['lo'] = t[j-1]['hi']
        t[0]['lo']  = float("-inf")
        t[len(t)-1]['hi'] =  float("inf")
        return t

    ranges1,j = [],0
    while j <= len(ranges0)-1:
        left = ranges0[j]
        right = None if j == len(ranges0)-1 else ranges0[j+1]
        if right:
            y = merge2(left['y'], right['y'])
            if y:
                j = j+1
                left['hi'], left['y'] = right['hi'], y
        ranges1.append(left)
        j = j+1
    return noGaps(ranges0) if len(ranges0)==len(ranges1) else mergeAny(ranges1)

def prune(rule, maxSize):
    n = 0
    for txt, ranges in rule.items():
        n = n + 1
        if(len(ranges) == maxSize[txt]):
            n = n+1
            rule[txt] = None
    if n > 0:
        return rule

def firstN(sort_ranges,s_fun):
    
    print(" ")
    def function(num):
        print(num['range']['txt'],
              num['range']['lo'],
              num['range']['hi'],
              rnd(num['val']),
              num['range']['y'].has)
    
    def useful(val):
        if val['val']> first_val/10 and val['val']>.05:
            return val
    
    _ = list(map(function, sort_ranges))
    print()
    
    first_val = sort_ranges[0]['val']
    sort_ranges = [x for x in sort_ranges if useful(x)]
    
    most,out = -1, -1
    for n in range(1,len(sort_ranges)+1):
        sliced_val = sort_ranges[0:n]
        slice_val_range = [x['range'] for x in sliced_val]
        temp,rule = s_fun(slice_val_range)
        if temp and temp > most:
            out,most = rule,temp
    
    return out,most