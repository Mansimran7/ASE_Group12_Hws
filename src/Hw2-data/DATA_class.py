import math
from cols_class import Cols
from row_class import Row
from utils import *
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
            return col.rnd(value, nPlaces), col.txt

        return kap(cols or self.cols.y, fun)
    
