import random
import sys
sys.path.append(sys.path[0]+'\\..\\src\\')
from num_class import Num
from sym_class import Sym
# from DATA_class import DATA
from utils import *
from misc import *
import math


def sym_test():
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
    print(mode,entropy)
    return (mode =="a" and 1.379 == rnd(entropy,3))

def num_test7():
    n = Num()
    for i in range(1,10+1):
        n.add(i)
    print("",n.n,n.mu,n.sd)
    return True

def ok_test(n=1):
    random.seed(n)
    return True

def sample_test():
    for i in range(1,10+1): 
        print("",''.join(samples(["a","b","c","d","e"]).values()))
    return True

def num_test():
    """
    Test for numbers
    
    Returns
    -------
    Bool
    """
    num1, num2 = Num(), Num()
    global Seed
    Seed = the['seed']
    for i in range(1,1001):
        num1.add(rand(0,1))
    Seed = the['seed']
    for i in range(1,1001):
        num2.add(rand(0,1)**2)
    m1,m2 = rnd(num1.mid(),1), rnd(num2.mid(),1)
    d1,d2 = rnd(num1.div(),1), rnd(num2.div(),1)
    print(1, m1, d1)
    print(2, m2, d2) 
    return m1 > m2 and 0.5 == rnd(m1,1)

def the_func():
    """
    Test for the
    
    Returns
    -------
    Bool
    """
    print(the)
    return True

def the_rand():

    """
    Runs all rand function
        
    Returns
    -------
    Bool
    """
    Seed = 1
    t=[]
    for i in range(1,1000+1):
        t.append(rint(0,100,1))
    u=[]
    for i in range(1,1000+1):
        u.append(rint(0,100,1))
    for k,v in enumerate(t):
        assert(v==u[k])

def num_chars(t):
    global n
    n = n + len(t)

def csv_test():
    csv(the['file'],num_chars)
    return n == 3192

def data_test():
    data = DATA(the['file'])
    col=data.cols.x[1]
    print(col.lo,col.hi,col.mid(),col.div())
    print(data.stats('mid', data.cols.y, 2))

def stats():
    data = DATA(the['file'])
    for k, cols in {'y': data.cols.y, 'x':data.cols.x}.items():
        print(k, 'mid',data.stats('mid',cols,2))
        print(' ','div', data.stats('div',cols,2))
    return True

def clone_test():
    data1 = DATA(the['file'])
    data2 = data1.clone(data1.rows)
    print(data1.stats('mid', data1.cols.y, 2))
    print(data2.stats('mid', data2.cols.y, 2))
    # return len(data1.rows) == len(data2.rows) and data1.cols.y[1].w == data2.cols.y[1].w and data1.cols.x[1].at == data2.cols.x[1].at and len(data1.cols.x) == len(data2.cols.x)

def around():
    data = DATA(the['file'])
    print(0,0,o(data.rows[1].cells))
    # print(0,0,data.rows[1].cells)
    for n,t in enumerate(data.around(data.rows[1])):
        if (n % 50) == 0:
            print(n, rnd(t['dist'],2) ,t['row'].cells)

def half_test():
    data = DATA(the['file'])
    left, right, A, B, mid, c = data.half()
    l,r = data.clone(left), data.clone(right)
    print(len(left),len(right))
    print(A.cells,c)
    print(mid.cells)
    print(B.cells)
    print("l",l.stats('mid', l.cols.y, 2))
    print("r",r.stats('mid', r.cols.y, 2))

def cluster():
    data = DATA(the['file'])
    show(data.cluster(),"mid",data.cols.y,1)

def optimize():
    data = DATA(the['file'])
    show(data.sway(),"mid",data.cols.y,1)

def every():
    repGrid(the['file'], DATA)

def position():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    rows.cluster()
    repPlace(rows)

def prototypes():
    t = dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    show(rows.cluster(),"mid",rows.cols.all,1)

def reprows():
    t=dofile(the['file'])
    rows = repRows(t, DATA, transpose(t['cols']))
    _ = list(map(oo, rows.cols.all))
    _ = list(map(oo, rows.rows))

def repcols():
    t = repCols(dofile(the['file'])['cols'], DATA)
    _ = list(map(oo, t.cols.all))
    _ = list(map(oo, t.rows))

def synonyms():
    data = DATA(the['file'])
    show(repCols(dofile(the['file'])['cols'], DATA).cluster(),"mid",data.cols.all,1)

def test_copy():
    t1 = {'a':1, 'b':{'c':2, 'd':[3]}}
    t2 = deepcopy(t1)
    t2['b']['d'][0] = 10000
    print('b4' , t1 , '\nafter' , t2)

def some_test():
    the['Max'] = 32
    num = Num()
    for i in range(1, 1001):
        num.add(i)
    print(num.has)

def dist_test():
    data = DATA(the['file'])
    num  = Num()
    for row in data.rows:
        num.add(data.dist(row, data.rows[1]))
    print({'lo' : num.lo, 'hi' : num.hi, 'mid' : rnd(num.mid(),3), 'div' : rnd(num.div(),3)})

def tree_test():
    data = DATA(the['file'])
    showTree(data.tree(),"mid",data.cols.y,1)
    return True

def sway_test():
    data = DATA(the['file'])
    best,rest,_ = data.sway()
    print("\nall ", data.stats('mid', data.cols.y, 2))
    print("    ", data.stats('div', data.cols.y, 2))
    print("\nbest",best.stats('mid', best.cols.y, 2))
    print("    ", best.stats('div', best.cols.y, 2))
    print("\nrest", rest.stats('mid', rest.cols.y, 2))
    print("    ", rest.stats('div', rest.cols.y, 2))

def bins_test():
    global b4
    data = DATA(the['file'])
    best,rest,_ = data.sway()
    print("all","","","",{'best':len(best.rows), 'rest':len(rest.rows)})
    for k,t in enumerate(bins(data.cols.x,{'best':best.rows, 'rest':rest.rows})):
        for range in t:
            if range['txt'] != b4:
                print("")
            b4 = range['txt']
            print(range['txt'],range['lo'],range['hi'],rnd(value(range['y'].has, len(best.rows),len(rest.rows),"best")),range['y'].has)

def test_xpln():
    data = DATA(the['file'])
    best,rest,evals = data.sway()
    rule,most= data.xpln(best,rest)
    print("\n-----------\nexplain=", data.showRule(rule))
    selects = data.selects(rule,data.rows)
    data_selects = [s for s in selects if s!=None]
    data1= data.clone(data_selects)
    print("all               ",data.stats('mid', data.cols.y, 2),data.stats('div', data.cols.y, 2))
    print("sway with",evals,"evals",best.stats('mid', best.cols.y, 2),best.stats('div', best.cols.y, 2))
    print("xpln on",evals,"evals",data1.stats('mid', data1.cols.y, 2),data1.stats('div', data1.cols.y, 2))
    top,_ = data.betters(len(best.rows))
    top = data.clone(top)
    print("sort with",len(data.rows),"evals",top.stats('mid', top.cols.y, 2),top.stats('div', top.cols.y, 2))

def cliffs_test():
    assert(False == cliffsDelta( [8,7,6,2,5,8,7,3],[8,7,6,2,5,8,7,3]))
    assert(True  == cliffsDelta( [8,7,6,2,5,8,7,3],[9,9,7,8,10,9,6])) 
    t1,t2=[],[]
    for i in range(1,1001):
        t1.append(rand(0,1))
    for i in range(1,1001):
        t2.append(rand(0,1)**.5)
    assert(False == cliffsDelta(t1,t1)) 
    assert(True  == cliffsDelta(t1,t2)) 
    diff,j=False,1.0
    while not diff:
        def function(x):
            return x*j
        t3=list(map(function, t1))
        diff=cliffsDelta(t1,t3)
        print(">",rnd(j),diff) 
        j=j*1.025

def gauss_test():
    t=[]
    for i in range(1,10**4+1):
        t.append(misc.gaussian(10,2))
    n=Num()
    for i in t:
        n.add(i)
    print("",n.n,n.mu,n.sd)
def bootmu_test():
    a, b = [], []
    for i in range(1, 101):
        a.append(misc.gaussian(10,1))
    print("","mu","sd","cliffs","boot","both")
    print("","--","--","------","----","----")
    while mu <= 11:
        b = []
        for i in range(1, 101):
            b.append(misc.gaussian(mu, 1))
        cl = misc.cliffsDelta(a, b)
        bs = misc.bootstrap(a, b)
        print("",mu,1,cl,bs,cl and bs)
        mu = mu + 0.1

def basic_test():
    print("\t\ttruee", bootstrap( {8, 7, 6, 2, 5, 8, 7, 3}, 
                                {8, 7, 6, 2, 5, 8, 7, 3}),
              cliffsDelta( {8, 7, 6, 2, 5, 8, 7, 3}, 
                           {8, 7, 6, 2, 5, 8, 7, 3}))
    print("\t\tfalse", bootstrap(  {8, 7, 6, 2, 5, 8, 7, 3},  
                                 {9, 9, 7, 8, 10, 9, 6}),
             cliffsDelta( {8, 7, 6, 2, 5, 8, 7, 3},  
                          {9, 9, 7, 8, 10, 9, 6})) 
    print("\t\tfalse", 
                    bootstrap({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, 
                               {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9}),
                  cliffsDelta({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, 
                              {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9}))

def pre_test():
    print("\neg3")
    d = 1
    tmp = False
    for i in range(1, 11):
        t1, t2 = [], []
        for j in range(1, 33):
            t1.append(misc.gaussian(10,1))
            t2.append(misc.gaussian(d*10, 1))
            if d < 1.1:
                tmp = True
            print("\t",d,tmp,bootstrap(t1,t2),bootstrap(t1,t1))
            d = d + 0.05

def five_test():
    for rx in tiles(scottKnot(
        [RX([0.34,0.49,0.51,0.6,.34,.49,.51,.6],"rx1"),
        RX([0.6,0.7,0.8,0.9,.6,.7,.8,.9],"rx2"),
        RX([0.15,0.25,0.4,0.35,0.15,0.25,0.4,0.35],"rx3"),
        RX([0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9],"rx4"),
        RX([0.1,0.2,0.3,0.4,0.1,0.2,0.3,0.4],"rx5")])):
        print(rx['name'], rx['rank'], rx['show'])

def six_test():
    for rx in tiles(scottKnot(
        [RX({101,100,99,101,99.5,101,100,99,101,99.5},"rx1"),
        RX({101,100,99,101,100,101,100,99,101,100},"rx2"),
        RX({101,100,99.5,101,99,101,100,99.5,101,99},"rx3"),
        RX({101,100,99,101,100,101,100,99,101,100},"rx4")])):
        print(rx['name'], rx['rank'], rx['show'])
    
def tiles_test():
    rxs, a, b, c, d, e, f, g, h, j, k = [], [], [], [], [], [], [], [], [], [], []
    for i in range(1, 1001):
        a.append(misc.gaussian(10,1))
    for i in range(1, 1001):
        b.append(misc.gaussian(10.1,1))
    for i in range(1, 1001):
        c.append(misc.gaussian(20,1))
    for i in range(1, 1001):
        d.append(misc.gaussian(30,1))
    for i in range(1, 1001):
        e.append(misc.gaussian(30.1,1))
    for i in range(1, 1001):
        f.append(misc.gaussian(10,1))
    for i in range(1, 1001):
        g.append(misc.gaussian(10,1))
    for i in range(1, 1001):
        h.append(misc.gaussian(40,1))
    for i in range(1, 1001):
        j.append(misc.gaussian(40,3))
    for i in range(1, 1001):
        k.append(misc.gaussian(10,1))
    for k, v in ([a, b, c, d, e, f, g, h, j, k]):
        rsx[k] = RX(v, "rx"+str(k+1))


def sk_test():
    rxs, a, b, c, d, e, f, g, h, j, k = [], [], [], [], [], [], [], [], [], [], []
    for i in range(1, 1001):
        a.append(misc.gaussian(10,1))
    for i in range(1, 1001):
        b.append(misc.gaussian(10.1,1))
    for i in range(1, 1001):
        c.append(misc.gaussian(20,1))
    for i in range(1, 1001):
        d.append(misc.gaussian(30,1))
    for i in range(1, 1001):
        e.append(misc.gaussian(30.1,1))
    for i in range(1, 1001):
        f.append(misc.gaussian(10,1))
    for i in range(1, 1001):
        g.append(misc.gaussian(10,1))
    for i in range(1, 1001):
        h.append(misc.gaussian(40,1))
    for i in range(1, 1001):
        j.append(misc.gaussian(40,3))
    for i in range(1, 1001):
        k.append(misc.gaussian(10,1))
    for k, v in ([a, b, c, d, e, f, g, h, j, k]):
        rsx[k] = RX(v, "rx"+str(k+1))
    for rx in tiles(scottKnot(rsx)):
        print(rx['rank'], rx['name'], rx['show'])
