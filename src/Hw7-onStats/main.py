from misc import *
import misc
from utils import *
import sys
# from DATA_class import *
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
    misc.eg('ok', 'ok', ok_test)
    misc.eg('sample', 'sample', sample_test)
    misc.eg('nums', 'nums', num_test7)
    misc.eg('gauss', 'gauss', gauss_test)
    misc.eg('bootmu', 'bootmu', bootmu_test)
    # misc.eg('basic', 'basic', basic_test)
    # misc.eg('pre', 'pre', pre_test)
    # misc.eg('five', 'five', five_test)
    # misc.eg('six', 'six', six_test)
    # misc.eg('tiles', 'tiles', tiles_test)
    # misc.eg('sk', 'sk', sk_test)
    main()