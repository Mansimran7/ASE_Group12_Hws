from num_class import Num
from sym_class import Sym
import re
import math

class Cols:
    def __init__(self,t):
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = None
        for n,s in enumerate(t):
            pattern = "^[A-Z]+"
            col_cond = re.search(pattern, s)
            if col_cond:
                col = Num(n,s)
            else:
                col = Sym(n,s)
            self.all.append(col)
            if not re.search("X$", s):
                if re.search("[!+-]$", s):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if re.search("!$", s):
                    self.klass = col
    
    def add(self,r):
        for t in [self.x, self.y]:
            for col in t:
                col.add(r.cells[col.at])