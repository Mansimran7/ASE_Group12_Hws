from misc import *
import misc
from utils import *
import sys
from DATA_class import *
sys.path.append(sys.path[0]+'\\..\\..\\tests\\')
from testEngine import *

def main():   
    saved={}
    fails=passing=0
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
                print('▶️ ',what,("-"*60))
                if egs[what]() == False:
                    fails += 1
                    print('❌ fail:	', what)
                else:
                    passing += 1
                    print('✅ pass:	', what)
    if fails+passing>0:
        print("🔆",{'pass' : passing, 'fail' : fails, 'success' : 100*passing/(passing+fails)//1})
    sys.exit(fails)

if __name__ == "__main__":
    misc.eg('the', 'show settings', the_func)
    misc.eg('rand','demo random number generation', the_rand)
    misc.eg('some','demo of reservoir sampling', some_test)
    misc.eg('nums','demo of NUM', num_test)
    misc.eg('syms', 'demo SYMS', sym_test)
    misc.eg('csv','reading csv files',csv_test)
    misc.eg('data','showing data sets',data_test)
    misc.eg('clone','replicate structure of a DATA',clone_test)
    misc.eg('cliffs','stats tests',cliffs_test)
    misc.eg('dist','distance test',dist_test)
    misc.eg('half','divide data in half',half_test)
    misc.eg('tree','make snd show tree of clusters',tree_test)
    misc.eg('sway','optimizing',sway_test)
    misc.eg('bins','find deltas between best and rest',bins_test)
    main()