from misc import *
import misc
from utils import *
import sys
sys.path.append(sys.path[0]+'\\..\\tests\\')
from testEngine import *

def main():   
    saved={}
    fails=0
    cli_var=cli(settings(help))
    for k,v in cli_var.items():
        the[k] = v
        saved[k] = v
    if the['help'] == True:
        print(help)
    else:
        for what,fun in egs.items():
            if the['go'] == 'all' or the['go'] == what:
                for k,v in saved.items():
                    the[k] = v
                Seed = the['seed']
                if egs[what]() == False:
                    fails += 1
                    print('❌ fail:	', what)
                else:
                    print('✅ pass:	', what)
    sys.exit(fails)

if __name__ == "__main__":
    misc.eg('the', 'show settings', the_func)
    #eg('rand', 'generate, reset, regenerate same', rand)
    misc.eg('sym', 'check syms', sym)
    misc.eg('num', 'check nums', num)
    main()