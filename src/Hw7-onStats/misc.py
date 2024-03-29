import utils
from help import *
import math
import random
import re
import sys
import copy
from num_class import Num
from copy import deepcopy
import json
from utils import *
# from DATA_class import DATA
from sym_class import Sym
from utils import *

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

def merge(rx1,rx2):
    
    rx3 = RX([], rx1['name'])
    rx3['has'] = rx1['has'] + rx2['has']
    rx3['has'] = sorted(rx3['has'])
    rx3['n'] = len(rx3['has'])
    return rx3

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

def samples(t, n=None):
    x = {}
    for i in range(1, (n or len(t)) + 1):
        x[i] = t[random.randint(0, len(t) - 1)]
    return x


def gaussian(mu, sd):
    mu, sd = mu or 0, sd or 1
    sq, pi, log, cos, r = math.sqrt, math.pi, math.log, math.cos, random.random
    return mu + sd * sq(-2 * log(r())) * cos(2 * pi * r())

def RX(tmp, s):
    t = sorted(tmp)

    return {'name': s or "", 'rank' : 0, 'n': len(t), 'show': "", 'has': t}

def mid(temp):
    t = temp['has'] if temp['has'] else temp
    n = len(t)//2
    if len(t)%2==0:
        return (t[n] +t[n+1])/2
    else:
        return t[n+1]

def div(temp):
    t= temp['has'] if temp['has'] else temp
    return (t[len(t)*(9//10)] - t[len(t)*(1//10)])/2.56


def scottKnot(rxs, NUM):

    def merges(i, j):
        output = RX([], rxs[i]['name'])
        for loop in range(i, j+1):
            output = merge(output, rxs[j])
        
        return output

    def same(low, cut, high):
        lower_value = merges(low, cut)
        higher_value = merges(cut+1, high)

        return cliffsDelta (lower_value['has'], higher_value['has']) and bootstrap(lower_value['has'], higher_value['has'], Num)

    def recurse(low, high, rank):
        before = merges(low, high)
        best_val = 0
        cut = None

        for loop in range(low, high+1):
            if loop < high:
                lower_value = merges(low, loop)
                higher_value = merges(loop+1, high)

                now = (lower_value['n']*(mid(lower_value) - mid(before))**2 + higher_value['n']*(mid(higher_value) - mid(before))**2) / (lower_value['n'] + higher_value['n'])

                if now > best_val:
                    if abs(mid(lower_value) - mid(higher_value)) >= cohen :
                        cut, best_val = loop, now
        
        if cut != None and not same(low, cut, high):
            rank = recurse(low, cut, rank) + 1
            rank = recurse(cut+1, high, rank)
        else:
            for i in range(low, high+1):
                rxs[i]['rank'] = rank
        return rank
    
    rxs = rxs_sort(rxs)
    cohen = div(merges(0, len(rxs)-1)) * the['cohen']
    recurse(0, len(rxs)-1, 1)

    return rxs


def rxs_sort(rxs):
    for loop_i, x in enumerate(rxs):
        for loop_j, y in enumerate(rxs):
            if mid(x) < mid(y):
                rxs[loop_j],rxs[loop_i]=rxs[loop_i],rxs[loop_j]
    return rxs

def tiles(rxs):

    inf = float('inf')
    low, high = inf, float('-inf')

    for rx in rxs:
        low, high = min(low,rx['has'][0]), max(high, rx['has'][len(rx['has'])-1])
    
    for rx in rxs:
        tmp, u = rx['has'], []
        
        def at(x):
            return tmp[of(len(tmp)*x//1, len(tmp))]
        def of(x,most):
            return int(max(0, min(most, x)))

        def pos(x):
            return math.floor(of(the['width']*(x-low)/(high-low+1E-32)//1, the['width']))

        for loop in range(1, the['width']+1):
            u.append(" ")
        
        a,b,c,d,e= at(.1), at(.3), at(.5), at(.7), at(.9) 
        A,B,C,D,E= pos(a), pos(b), pos(c), pos(d), pos(e)

        for loop_i in range(A, B+1):
            u.append("-")
        
        for loop_i in range(D, E+1):
            u.append("-")        
        u[the['width']//2] = "|" 
        u[C] = "*"
        x = []

        for i in [a,b,c,d,e]:
            x.append(the['Fmt'].format(i))
        rx['show'] = ''.join(u) + str(x)
    
    return rxs

def delta(i, other):
    e, y, z= 1E-32, i, other
    return abs(y.mu - z.mu) / ((e + y.sd**2/y.n + z.sd**2/z.n)**.5)

def bootstrap(y_val, z_val, Num):
    x, y, z, yhat, zhat = Num(), Num(), Num(), [], []

    for y1 in y_val:
        x.add(y1)
        y.add(y1)
    
    for z1 in z_val:
        x.add(z1)
        z.add(z1)
    
    xmu, ymu, zmu = x.mu, y.mu, z.mu

    for y1 in y_val:
        yhat.append(y1 - ymu + xmu)
    for z1 in z_val:
       zhat.append(z1 - zmu + xmu)
    
    tobs = delta(y,z)
    n = 0

    for loop in range(1, 1,the['bootstrap']+1):
        val = Num()
        tmp = Num()

        for y in samples(yhat).values():
            val.add(y)
        
        for z in samples(zhat).values():
            tmp.add(z)
        
        if delta(val, tmp) > tobs:
            n = n + 1
    return n / the['bootstrap'] >= the['conf']