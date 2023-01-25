from help import *
import math
import re
import sys

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
   