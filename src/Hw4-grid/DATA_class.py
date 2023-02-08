import math
from cols_class import Cols
from row_class import Row
from utils import *
from utils import rnd
from misc import *

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

        return kap(cols or self.cols.y, fun)
    
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
            d = d + math.pow(col.dist(row1.cells[col.at], row2.cells[col.at]), the['p']) 
        return math.pow((d/n), 1/the['p'])

    def around(self, row1, rows = None, cols = None):
        def temp(row2):
            return {'row' : row2, 'dist' : self.dist(row1,row2,cols)} 
        return sorted(list(map(temp, rows or self.rows)), key = lambda k : k["dist"])

    
    def half(self, rows = None, cols = None, above = None):
        def project(row):
            return {'row' : row, 'dist' : cosine(dist(row,A), dist(row,B), c)}
        
        def dist(row1,row2): 
            return self.dist(row1,row2,cols)
        
        rows = rows or self.rows
        some = many(rows,the['Sample'])
        A = above or any(some)
        B = self.around(A,some)[int(the['Far'] * len(rows))//1]['row']
        c = dist(A,B)
        left, right = [], []
        
        pairs_of_prows = sorted(list(map(project, rows)), key=lambda k: k["dist"])
        
        for n, temp in enumerate(pairs_of_prows):
            if   n <= len(rows) // 2:
                left.append(temp["row"])
                mid = temp["row"]
            else:
                right.append(temp["row"])
        
        return left, right, A, B, mid, c

    def cluster(self, rows = None, min = None, cols = None, above = None):
        rows = rows or self.rows
        min = min or ((len(rows))**the['min'])
        cols = cols or self.cols.x
        node = {'data' : self.clone(rows)}
        if len(rows) > 2*min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows, cols, above)
            node['left'] =  self.cluster(left, min, cols, node['A'])
            node['right'] = self.cluster(right, min, cols, node['B'])
        return node
        

    def sway(self, rows = None, min = None, cols = None, above = None):
        rows = rows or self.rows
        min = min or math.pow(len(rows), the['min'])
        cols = cols or self.cols.x
        node = {'data' : self.clone(rows)}
        if len(rows) > 2*min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows,cols,above)
            if self.better(node['B'],node['A']):
                left,right,node['A'],node['B'] = right,left,node['B'],node['A']
            node['left']  = self.sway(left,  min, cols, node['A'])
        return node
