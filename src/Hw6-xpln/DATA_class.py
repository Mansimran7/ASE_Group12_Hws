import math
from cols_class import Cols
from row_class import Row
from utils import *
from utils import rnd
from misc import *
from operator import itemgetter

class DATA:
    
    """
    A class to represent many rows, summarized into columns

    """

    def __init__(self, src):

        self.rows = []
        self.cols = None
        
        if type(src) == str:
            csv(src, self.add)
        else:
            for row in src:
                self.add(row)
        

    def add(self, t):
        if self.cols:
            t = Row(t) if type(t) == list else t
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = Cols(t)
    
    def clone(self, init = {}):
        data = DATA([self.cols.names])
        def push(x):
            data.add(x)
        list(map(push, init))
        return data

    def stats(self, what, cols, nPlaces):

        def fun(_, col):
            if what == 'div':
                value = col.div()
            else:
                value = col.mid()
            rounded_value = col.rnd(value, nPlaces)
            return rounded_value, col.txt

        return misc.kap(cols or self.cols.y, fun)
    
    def better(self, row1, row2):
        
        s1,s2,ys = 0,0,self.cols.y
        for col in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])

            s1 = s1 - math.exp(col.w * (x-y) / len(ys))
            s2 = s2 - math.exp(col.w * (y-x) / len(ys))
        
        return s1/len(ys) < s2/len(ys)

    def dist(self, row1, row2, cols = None):
        n,d = 0,0
        for col in cols or self.cols.x:
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**the['p']
        return math.pow((d/n), 1/the['p'])

    def around(self, row1, rows = None, cols = None):
        def temp(row2):
            return {'row' : row2, 'dist' : self.dist(row1,row2,cols)} 
        return sorted(list(map(temp, rows or self.rows)), key = lambda k : k["dist"])
    
    def furthest(self, row1, rows = None, cols = None):
        t = self.around(row1,rows,cols)
        return t[len(t)-1]

    def half(self, rows = None, cols = None, above = None):
        def project(row):
            return {'row' : row, 'dist' : misc.cosine(gap(row,A), gap(row,B), c)}

        def gap(r1,r2): 
            return self.dist(r1,r2,cols)

        def function(r):
            return {'row' : r, 'dist' : gap(r, A)}

        rows = rows or self.rows
        some = misc.many(rows,the['Halves'])
        A    = above if above and the['Reuse'] else misc.any(some)
        temp = sorted(list(map(function, some)), key = lambda k : k["dist"])
        far = temp[int(the['Far'] * len(rows))//1]
        B    = far['row']
        c    = far['dist']
        left, right = [], []

        for n,temp in enumerate(sorted(list(map(project, rows)), key = lambda k : k["dist"])):
            if n < len(rows)//2:
                left.append(temp['row'])
            else:
                right.append(temp['row'])

        evals = 1 if the['Reuse'] and above else 2
        return left, right, A, B, c, evals

    def cluster(self, rows = None, cols = None, above = None):
        rows = rows or self.rows
        # mid = mid or ((len(rows))**the['mid'])
        cols = cols or self.cols.x
        node = {'data' : self.clone(rows)}
        if len(rows) >= 2:
            left, right, node['A'], node['B'], node['mid'], node['c'] = self.half(rows, cols, above)
            node['left'] =  self.cluster(left, cols, node['A'])
            node['right'] = self.cluster(right, cols, node['B'])
        return node

    def tree(self, rows = None , mini = None, cols = None, above = None):
        rows = rows or self.rows
        mini  = mini or len(rows)**the['min']
        cols = cols or self.cols.x
        node = { 'data' : self.clone(rows) }
        if len(rows) >= 2*mini:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows,cols,above)
            node['left']  = self.tree(left,  mini, cols, node['A'])
            node['right'] = self.tree(right, mini, cols, node['B'])
        return node
    
    def sway(self):
        data = self
        def worker(rows, worse, evals = None, above = None):
            if len(rows) <= len(data.rows)**the['min']: 
                return rows, misc.many(worse, the['rest']*len(rows)), evals
            else:
                l,r,a,b,c,evals1 = self.half(rows, None, above)
                if self.better(b,a):
                    l,r,a,b = r,l,b,a
                for row in r:
                    worse.append(row)
                return worker(l,worse,evals+evals1,a)
        best,rest,evals1 = worker(data.rows,[],0)
        return self.clone(best), self.clone(rest), evals1
    
    def RULE(ranges, maxSize):
        t = {}
        for range in ranges:
            t[range['txt']] = t.get(range['txt']) or []
            t[range['txt']].append({'lo' : range['lo'],'hi' : range['hi'],'at':range['at']})
        return misc.prune(t, maxSize)

    def showRule(self, rule):
        def pretty(range):
            return range['lo'] if range['lo'] == range['hi'] else [range['lo'], range['hi']]
        def merge(t0):
            t,j = [],1
            while j <= len(t0):
                
                left = t0[j-1]
                if j < len(t0):
                    right = t0[j]
                else:
                    right = None                
                
                if right and left['hi'] == right['lo']:
                    left['hi'] = right['hi']
                    j = j + 1
                t.append({'lo' :left['lo'], 'hi' : left['hi']})
                j = j + 1
            return t if len(t0)==len(t) else merge(t)
        def merges(attr, ranges):
            return list(map(pretty, merge(sorted(ranges, key = itemgetter('lo'))))), attr
        
        return misc.dkap(rule, merges)

    def better(self, row1, row2):
        s1, s2, ys = 0, 0, self.cols.y
        for _,col in enumerate(ys):
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])
            s1 = s1 - math.exp(col.w * (x-y)/len(ys))
            s2 = s2 - math.exp(col.w * (y-x)/len(ys))
        return s1/len(ys) < s2/len(ys)

    def xpln(self, best, rest):

        def v(has):
            return misc.value(has, len(best.rows), len(rest.rows), "best")
        
        def score(ranges):
            rule = DATA.RULE(ranges, maxSizes)
            
            if rule:
                print(self.showRule(rule))
                bestr = self.selects(rule, best.rows)
                restr = self.selects(rule, rest.rows)

                if (len(bestr) + len(restr)) > 0:
                    return v({best: len(bestr), rest:len(restr)}), rule

        tmp,maxSizes = [],{}
        for ranges in misc.bins(self.cols.x,{'best':best.rows, 'rest':rest.rows}):
            maxSizes[ranges[1]['txt']] = len(ranges)
            print("") 

            for range in ranges:
                print(range['txt'], range['lo'], range['hi'])
                tmp.append({'range':range, 'max':len(ranges),'val': v(range['y'].has)})
            
        
        rule,most=misc.firstN(sorted(tmp, key=itemgetter('val')),score) 

        return rule, most

    def selects(self, rule, rows):
        def disjunction(ranges, row):
            for range in ranges:
                lo, hi, at = range['lo'], range['hi'], range['at']
                x = row.cells[at]
                if x == "?":
                    return True
                if lo == hi and lo == x:
                    return True
                if lo <= x and x < hi:
                    return True
            return False

        def conjunction(row):
            for ranges in rule.values():
                if not disjunction(ranges, row):
                    return False
            return True

        def function(r):
            if conjunction(r):
                return r

        return list(map(function, rows))