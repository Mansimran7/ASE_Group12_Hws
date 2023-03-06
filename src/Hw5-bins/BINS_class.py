import math
from cols_class import Cols
from row_class import Row
from utils import *
from utils import rnd
from misc import *

class BINS:
    def __init__(self, cols, rowss):
        out = {}
        for _,col in cols:
            ranges = {}
            for y, rows in rowss:
                for _, row in rows:
                    x, k = row[col.at]
                    if x!= "?":
                        k = self.bin(col, x)
                        ranges[k] = ranges[k] or RANGE(col.at, col.txt, x)
                        extend(ranges[k], x, y)
            ranges = sort(map(ranges, itself), lt["l"])
            out[1 + len(out)] = col.isSym and ranges or mergeAny(ranges)
        return out 