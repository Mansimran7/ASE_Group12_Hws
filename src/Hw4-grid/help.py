"""
Help
-------------------------
It is a header string showing help, from which we build our 'the' settings object

"""
the = {
    'dump': False,
    'go': None,
    'seed': 937162211,
}

help="\n\
gird.lua : a rep grid processor \n\
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 \n\
USAGE: grid.lua  [OPTIONS] [-g ACTION] \n\
OPTIONS: \n\
  -d  --dump    on crash, dump stack   = false \n\
  -f  --file    name of file           = ../../etc/data/repgrid1.csv \n\
  -g  --go      start-up action        = data \n\
  -h  --help    show help              = false \n\
  -p  --p       distance coefficient   = 2 \n\
  -s  --seed    random number seed     = 937162211 \n\
ACTIONS: \n\
"
Seed = 937162211

egs={}

n = 0