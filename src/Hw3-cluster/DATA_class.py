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
    

    def clone(self, init, data):
        data = DATA({self.cols.name})
        def push(x):
            data.add(x)
        map(init or {}, push)
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
    
    def better(self, row1, row2, s1, s2, ys, x, y):
        
        s1,s2,ys = 0,0,self.cols.y
        for key, col in ys:
            x = col.norm(row1.cells[col.at])
            y = col.norm(row2.cells[col.at])

            s1 = s1 - math.exp(col.w * (x-y) / len(ys))
            s2 = s2 - math.exp(col.w * (y-x) / len(ys))
        
        return s1/len(ys) < s2/len(ys)

    def dist(self, row1, row2, cols, n,d):

        n,d = 0,0
        for key, col in cols or self.cols.x:
            n = n + 1
            d = d + math.pow(col.dist(row1.cells[col.at], row2.cells[col.at]), the['p']) 

        return math.pow((d/n), 1/the['p'])

    def sway(self, rows, min, cols, above):

        rows = rows or self.rows
        min = min or math.pow(len(rows), the['min'])
        cols = cols or self.cols.x
        node = {'data' : self.clone(rows)}

        if len(rows) > 2*min:
            left, right, node['A'], node['B'], node['mid'] = self.half(rows,cols,above)
            if self.better(node['B'],node['A']):
                left,right,node['A'],node['B'] = right,left,node['B'],node['A']
            node['left']  = self.sway(left,  min, cols, node['A'])
        
        return node

